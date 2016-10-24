
class MyDec(object):
    """docstring for MyDec"""

    @staticmethod
    def dec_test(fn):
        def wrap(self):
            print "begin"
            self.another_func()
            fn(self)
            print "over"
        return wrap

    @staticmethod
    def dec_test_arg(fn):
        def wrap(self, *arg, **kwargs):
            print "dec_arg begin"
            self.another_func()
            fn(self, *arg, **kwargs)
            print "dec_arg over"
        return wrap

    @staticmethod
    def dec_test_return(fn):
        def wrap(self, *arg, **kwargs):
            print "dec_return begin"
            ret = fn(self, *arg, **kwargs)
            print "dec_return end"
            return ret
        return wrap

    @classmethod
    def dec_test2(cls, fn):
        def wrap(self):
            print "begin"
            self.another_func()
            fn(self)
            print "over"
        return wrap

    def another(self):
        print "test another func"


class MyClass(object):
    """docstring for MyClass"""

    def __init__(self, arg):
        super(MyClass, self).__init__()
        self.arg = arg

    def another_func(self):
        print "another_func"

    @MyDec.dec_test
    def test(self):
        print "##test"

    @MyDec.dec_test2
    def test2(self):
        print "##test2"

    @MyDec.dec_test_arg
    def test_with_arg(self, *arg, **kwargs):
        print "##test_with_arg"
        # print "arg:%s" % arg
        print "arg:%s" % str(arg)
        print "kwargs:%s" % str(kwargs)
        print "a: %s" % kwargs.get("a")
        print "b: %s" % kwargs.get("b")

    @MyDec.dec_test_return
    def test_with_return(self, *arg, **kwargs):
        print "##test_with_return"
        return str(arg)


class SubClass(MyClass):
    """docstring for SubClass"""

    def __init__(self, arg):
        super(SubClass, self).__init__(arg)
        self.arg = arg

    def test(self):
        print "sub test"


if __name__ == '__main__':
    # a = MyClass(1)
    # a.test()
    # a.test_with_arg(12, 45)
    # print a.test_with_return(4234, 423)
    # a.test2()
    b = SubClass(2)
    b.test()
    b.test_with_arg(a="sub", b="class")
