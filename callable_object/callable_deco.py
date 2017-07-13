class EnterExitParam(object):

    def __init__(self, p1):
        self.p1 = p1

    def __call__(self, f):
        def new_f():
            print("Entering", f.__name__)
            print("p1=", self.p1)
            f()
            print("Leaving", f.__name__)
        return new_f


@EnterExitParam("foo bar")
def hello():
    print("Hello")


if __name__ == "__main__":
    hello()
