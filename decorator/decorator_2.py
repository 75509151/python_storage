# class bDecorator(object):

#     def __init__(self, fn):
#         print "inside myDecorator.__init__()"
#         self.fn = fn

#     def prompt(self, fn):
#         print "prompt"

#     def __call__(self):
#         self.fn()
#         print "inside myDecorator.__call__()"

# # bD = bDecorator(1)


def dec_test(fn):
    def wrap(self, arg):
        print "begin"
        self.another_func()
        fn(arg)
        print "over"
    return wrap


def dec_test_arg(fn):
    def wrap(self, *arg, **kwargs):
        print "dec_arg begin"
        self.another_func()
        fn(arg, kwargs)
        print "dec_arg over"
    return wrap


def dec_test_return(fn):
    def wrap(self, *arg, **kwargs):
        print "dec_return begin"
        ret = fn(arg, kwargs)
        print "dec_return end"
        return ret
    return wrap


class MyClass(object):
    """docstring for MyClass"""

    def __init__(self, arg):
        super(MyClass, self).__init__()
        self.arg = arg

    def another_func(self):
        print "another_func"

    # @bDecorator.prompt
    @dec_test
    def test(self):
        print "##test"

    @dec_test_arg
    def test_with_arg(self, *arg, **kwargs):
        print "##test_with_arg"
        print "arg:%s" % str(arg)
        print "kwargs: %s" % str(kwargs)

    @dec_test_return
    def test_with_return(self, *arg, **kwargs):
        print "##test_with_return"
        return 1


if __name__ == '__main__':
    a = MyClass(1)
    a.test("fsdf")
    a.test_with_arg("nihao")
    res = a.test_with_return()
    print "return: %s" % res
