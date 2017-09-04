# coding: utf-8
import compileall
import os
import shutil
import subprocess
import sys
import glob
import hashlib


def get_bool_input():
    yes = set(['yes', 'y', 'y'])
    no = set(['no', 'n'])
    while True:
        choice = raw_input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print "Please respond with 'yes' or 'no'"


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


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


def _split_file(file, todir, prefix="x", block_size="1m", suffix_length=4):
    if os.path.exists(todir):
        print "输出路径的文件夹存在，需要删除文件夹吗？[y/n]"
        if get_bool_input():
            shutil.rmtree(todir)
            os.makedirs(todir)
        else:
            sys.exit(0)
    else:
        os.makedirs(todir)
    os.chdir(todir)
    return_code, out, err = do_cmd("split -b {block_size} {file} -d -a {suffix_length} {prefix}".format(
        block_size=block_size,
        file=file,
        suffix_length=suffix_length,
        prefix=prefix))
    if return_code or err:
        raise Exception(err)
    return True


def _generate_download_info(splited_files_path, files_prefix="kiosk", version=""):
    files = glob.glob(os.path.join(splited_files_path, files_prefix + "*"))
    info_dict = {}
    info_dict = {"files_count": len(files)}
    for file in files:
        file_md5 = md5(file)
        _, file_name = os.path.split(file)
        info_dict[file_name] = file_md5

    info_file = os.path.join(splited_files_path, "version_info.json")
    print info_dict
    import json
    with open(info_file, "w") as f:
        json.dump(info_dict, f)


if __name__ == '__main__':
    # _check_project("/home/mm/code/kiosk")
    # release_project("/home/mm/code/kiosk", "/home/mm/code/kiosk_release")
    # _pack_project("/home/mm/code/kiosk", "/home/mm/code/test/kiosk_121.tgz")
    # creat_version("/home/mm/code/kiosk", "/home/mm/code/test", version="1.2.1")
    # _split_file("/home/mm/code/test/kiosk_121.tgz", "/home/mm/code/test/version121/", prefix="kiosk")
    _generate_download_info("/home/mm/code/test/version121/", files_prefix="kiosk")
    print "end"
