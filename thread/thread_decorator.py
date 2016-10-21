import unittest
import threading
import time


def run_in_thread(fn):
    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run


# class MyTest(unittest.TestCase):
#     """docstring for MyTest"""

#     def __init__(self, arg):
#         super(MyTest, self).__init__()
#         self.arg = arg

class MyTest(object):
    """docstring for MyTest"""

    def __init__(self):
        super(MyTest, self).__init__()

    @run_in_thread
    def hehe(self):
        time.sleep(3)
        print "hehe"


@run_in_thread
def test_run_in_thread():
    time.sleep(6)
    print "sleep over"


if __name__ == '__main__':
    test_run_in_thread()
    a = MyTest()
    a.hehe()
    print "haha"
    while True:
        time.sleep(1)
