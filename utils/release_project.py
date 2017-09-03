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


if __name__ == '__main__':
    release_project("/home/mm/code/kiosk", "/home/mm/code/kiosk_release")
