# coding: utf-8
# need work with release_project
import os
import shutil
import subprocess
import sys
import glob
import hashlib
import json


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def do_cmd(cmd):
    print "do cmd: %s" % cmd
    child = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    child.wait()
    out = child.stdout.read()
    err = child.stderr.read()
    return child.returncode, out, err


def _sync_version_all(remote_path, local_path):
    print remote_path, local_path
    returncode, out, err = do_cmd("rsync -az --delete {remote_path} {local_path}".format(
        remote_path=remote_path, local_path=local_path))
    print "returncode", returncode
    print "out", out
    print "err", err


def _sync_version_part(remote_file, local_path):
    pass


def _sync_download_info(remote_path, local_path):
    print "_sync_download_info begin"
    download_info = os.path.join(remote_path, "version_info.json")
    returncode, out, err = do_cmd("rsync -az --delete {download_info} {local_path}".format(
        download_info=download_info, local_path=local_path))
    print "returncode", returncode
    print "out", out
    print "err", err
    print "_sync_download_info end"
    return download_info


def _check_md5(local_path, prefix="kiosk"):
    print "check md5 begin"
    download_info_filename = os.path.join(local_path, "version_info.json")
    download_info = {}
    with open(download_info_filename, "r") as f:
        download_info = json.load(f)
    need_check_files = glob.glob(os.path.join(local_path, "kiosk*"))
    # print need_check_files
    if len(need_check_files) != download_info["files_count"]:
        print "miss some files"
        return False
    for file in need_check_files:
        _, file_name = os.path.split(file)
        try:
            if download_info[file_name] == md5(file):
                continue
            else:
                return False
        except Exception as e:
            print "check md5 err:%s" % str(e)
            return False
    print "check md5 ok"
    return True


def sync_version(remote_path, local_path, version=""):
    version = version.replace(".", "")
    remote_version_path = os.path.join(remote_path, "version" + version)
    if not remote_version_path[-1] == "/":
        remote_version_path += "/"
    version_info = _sync_download_info(remote_version_path, local_path)
    version_info_dic = {}
    with open(version_info, "r") as f:
        version_info_dic = json.load(f)
    if version_info:
        print "version_info_dic", version_info_dic
    else:
        raise Exception("can not get version_info file")
    _sync_version_all(remote_version_path, local_path)
    if _check_md5(local_path):
        print "sync_version ok"
        return True
    else:
        print "sync_version failed"
        return False


def cat_split_files_to_file(local_path, file_name="kiosk.tgz", prefix="kiosk"):
    print "cat files begin"
    splited_files = os.path.join(local_path, prefix + "*")
    file = os.path.join(local_path, file_name)
    # returncode, out, err = do_cmd("cat {splited_files} > {file}".format(
    #     splited_files=splited_files, file=file))
    # if returncode or err:
    #     print "returncode: %s, err: %s" % (returncode, err)
    os.system("cat {splited_files} > {file}".format(splited_files=splited_files, file=file))
    print "cat files end. to: %s" % file
    return file


def sync_version_retry():
    pass


def package_download(remote_path, local_path, version):
    sync_version(remote_path, local_path, version=version)
    package = cat_split_files_to_file(local_path)
    print md5(package)


if __name__ == '__main__':
    remote_path = "/home/mm/code/test/"
    local_path = "/home/mm/code/test/local/"
    package_download(remote_path, local_path, version="1.2.1")
