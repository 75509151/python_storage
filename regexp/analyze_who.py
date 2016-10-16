#!/bin/python
from subprocess import Popen
import os
import re

file_path = os.path.join("/home/mm", "test_who.txt")

p = Popen("who", shell=True, stdout=open(file_path, "w"), stderr=open("/dev/null", "w"))
a = p.wait()
print "return code:" + str(a)


with open(file_path, "r") as f:
    for each_line in f.readlines():
        print each_line
        print re.split(r'\s{2,}', each_line.strip())

        print '\n'


#! /usr/bin/python
from os import popen
from re import split

f = popen('who', 'r')
for eachLine in f.readlines():
    print split(r'\s\s+|\t', eachLine.strip())
f.close()
