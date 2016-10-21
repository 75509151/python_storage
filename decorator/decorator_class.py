import unittest


class myDecorator(object):

    def __init__(self, fn):
        print "inside myDecorator.__init__()"
        self.fn = fn

    def __call__(self):
        self.fn()
        print "inside myDecorator.__call__()"


@myDecorator
def aFunction():
    print "inside aFunction()"


@myDecorator
def bFunction():
    print "b"

print "Finished decorating aFunction()"


if __name__ == '__main__':
    aFunction()
    # a = MyClass(1)
    # a.test("fsdf")
