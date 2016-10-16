#!/bin/python
import re
import os


def head(arg):
    print "#" * 20
    print " " * 10 + arg
    print "#" * 20


head("search interge")
file_path = os.path.join("/home/mm/code_depot/python/regexp/", "base.txt")
file_mode = "r"
pattern = r'^\d+$'
pattern1 = r'^[1-9][0-9]*$'
name_pattern = r'^(?P<int>\d+)$'
negative = r'^-[1-9][0-9]*$'

with open(file_path, file_mode) as f:
    for each_line in f.readlines():
        # print each_line
        match = re.search(pattern1, each_line)
        m = re.search(name_pattern, each_line)
        negative_m = re.search(negative, each_line)
        if negative_m:
            print negative_m.group(0)
        if match:
            # print match.group(0)
            print m.group("int")

# http://kiritor.blog.51cto.com/7400479/1226676
head("search name")
name_pattern = r'name\s*:\s*(?P<first_name>(\w+\s+)+)(?P<last_name>\w+)'
with open(file_path, file_mode) as f:
    for each_line in f.readlines():
        m = re.search(name_pattern, each_line)
        if m:
            print 'frist_name:' + m.group('first_name') + ',last_name:' + m.group('last_name')

head("search valid password ")
pwd = r'^([a-zA-Z0-9]|_)\w{7,10}$'  # user password length is  8 to 10( only begin with letter, number, underscores)
chinese_pwd = r'^[\u4e00-\u9fa5]{0,}$'  # i can't confirm it's right
with open(file_path, file_mode) as f:
    for each_line in f.readlines():
        m = re.search(pwd, each_line)
        chinese_m = re.search(chinese_pwd, each_line)
        if m:
            print m.group(0)
        if chinese_m:
            print chinese_m.group(0)
