# import compileall
# compileall.compile_dir('/home/mm/code/kiosk', ddir="/home/mm/output_dir")
# python -m compileall $dir

import py_compile
import os
import glob
import shutil


def check_and_ajust_dir(dir_path, check_exist=True):

    if not dir_path.startswith("/"):
        raise ValueError("must be absolute path")
    if not dir_path.endswith("/"):
        dir_path += "/"
    if check_exist and not os.path.isdir(dir_path):
        raise ValueError("path does not exist: %s" % dir_path)
    return dir_path


def get_relative_file_in_project(project_path, file):
    if not file.startswith(project_path):
        raise ValueError("this file does not in project: %s" % file)
    else:
        return file[len(project_path):]


this_file = os.path.abspath(__file__)
print this_file
this_dir = os.path.dirname(this_file)
print this_dir


project_path = '/home/mm/code/kiosk'

project_path = check_and_ajust_dir(project_path)

print project_path

project_name = os.path.basename(project_path)
output_dir = os.path.join(project_path, "complite_dir")

if os.path.exists(output_dir):
    os.rmdir(output_dir)


all_py = []
for (dirpath, dirnames, filenames) in os.walk(project_path):
    # print dirpath, dirnames, filenames
    py_files = [os.path.join(dirpath, file) for file in filenames if file.endswith(".py")]
    # print py_files
    all_py += py_files

for py_file in all_py:
    relative_file = get_relative_file_in_project(project_path, py_file)
    pyc_file = os.path.join(output_dir, relative_file + "c")
    pyc_path = os.path.dirname(pyc_file)
    if not os.path.exists(pyc_path):
        os.makedirs(pyc_path)
    # print pyc_file, relative_file
    # break
    py_compile.compile(py_file, pyc_file)
