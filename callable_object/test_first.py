import unittest


class BasePreProcess(object):
    def __init__(self, *arg):
        super(BasePreProcess, self).__init__()
        self.arg = arg
        self.__call__()

    def do_action(self):
        print str(self.arg) + ":do do do "

    def __call__(self):
        self.do_action()


class CallTest(unittest.TestCase):
    """docstring for CallTest"""

    def test_call_drect(self):
        BasePreProcess("1")
        # print a.do_action()

    def test_do_do(self):
        a = BasePreProcess("2")
        print a.do_action()


if __name__ == '__main__':
    unittest.main()
