#!/usr/bin/python
import hashlib
import sys
import os


def get_file_md5(file_path):
    m = hashlib.md5()

    with open(file_path, "rb") as f:
        while True:
            data = f.read()
            if data:
                m.update(data)
            else:
                break
    return m.hexdigest()


def get_file_md5_test(path):
    pass


if __name__ == "__main__":
    argv_len = len(sys.argv)
    print "argv_len: %s" % argv_len
    if argv_len != 2:
        print "wrong argv_len"
    else:
        path = sys.argv[1]
        print "file name: %s" % path
        print "md5: %s" % get_file_md5(path)
