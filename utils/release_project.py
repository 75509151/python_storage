import compileall
import os
import shutil
import subprocess


def do_cmd(cmd):
    child = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    child.wait()
    out = child.stdout.read()
    err = child.stderr.read()
    return child.returncode, out, err


def _check_project(project_path):
    os.chdir(project_path)
    return_code, out, err = do_cmd("svn update")
    if return_code != 0 or err:
        raise Exception(err)

    return_code, out, err = do_cmd("svn status")
    if return_code != 0 or err:
        raise Exception(err)
    if out:
        raise Exception("project not clean: %s" % out)
    return True


def _complite_project(project_path):
    compileall.compile_dir(project_path)


def _clean_project(project_path):
    def clean_py():
        all_py = []
        for (dirpath, dirnames, filenames) in os.walk(project_path):
            # print dirpath, dirnames, filenames
            all_py += [os.path.join(dirpath, file) for file in filenames if file.endswith(".py")]

        for py_file in all_py:
            os.remove(py_file)
    clean_py()


def _cp_project(project_path, output_path):
    shutil.copytree(project_path, output_path)


def release_project(project_path, output_path, svn_check=True):
    if svn_check:
        _check_project(project_path)
    _cp_project(project_path, output_path)
    _complite_project(output_path)
    _clean_project(output_path)


def creat_version(project_path, output_path, version, prefix="kiosk"):
    version = version.replace(".", "")
    pack_name = os.path.join(output_path, prefix + "_" + version + ".tgz")
    print pack_name
    _pack_project(project_path, pack_name)
    project_tgz = pack_name
    _split_file(project_tgz)


def _pack_project(project_path, pack_name):
    os.system("tar -cvzf {pack_name} {project_path}".format(pack_name=pack_name, project_path=project_path))


def _split_file(file, todir, prefix="x", block_size="1m", suffix_length=3):
    os.chdir(todir)
    return_code, out, err = do_cmd("split -b {block_size} {file} -d -a {suffix_length} {prefix}".format(
        block_size=block_size,
        file=file,
        suffix_length=suffix_length,
        prefix=prefix))
    print return_code, out, err


if __name__ == '__main__':
    # _check_project("/home/mm/code/kiosk")
    # release_project("/home/mm/code/kiosk", "/home/mm/code/kiosk_release")
    # _pack_project("/home/mm/code/kiosk", "/home/mm/code/test/kiosk_121.tgz")
    # creat_version("/home/mm/code/kiosk", "/home/mm/code/test", version="1.2.1")
    _split_file("/home/mm/code/test/kiosk_121.tgz", "/home/mm/code/test/", prefix="kiosk")
    print "end"
