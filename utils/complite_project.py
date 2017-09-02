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
    shutil.rmtree(output_dir)


all_file = []
for (dirpath, dirnames, filenames) in os.walk(project_path):
    # print dirpath, dirnames, filenames
    all_file += [os.path.join(dirpath, file) for file in filenames]

for file in all_file:

    def deal_py(py_file):

        relative_file = get_relative_file_in_project(project_path, py_file)
        pyc_file = os.path.join(output_dir, relative_file + "c")
        pyc_path = os.path.dirname(pyc_file)
        if not os.path.exists(pyc_path):
            os.makedirs(pyc_path)
        # print pyc_file, relative_file
        # break
        py_compile.compile(py_file, pyc_file)

    def deal_other(other_file):
        relative_file = get_relative_file_in_project(project_path, other_file)
        other_path_file = os.path.join(output_dir, relative_file)
        output_path = os.path.dirname(other_path_file)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        shutil.copyfile(other_file, other_path_file)

    if file.endswith(".py"):
        deal_py(file)
    else:
        deal_other(file)

print "end"
