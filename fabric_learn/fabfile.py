from fabric.api import local
from first.deploy import *
from first.task_test import *


def hello(name="world"):
    # fab hello:nihao
    # fab hello:name=nihao
    print("Hello %s!" % name)


def local_test():
    local("python ./first/first.py")
