
class Base(object):
    def __init__(self):
        print "enter Base"
        print "leave Base"


class A(Base):
    def __init__(self):
        print "enter A"
        super(A, self).__init__()
        print "leave A"


class B(A):
    def __init__(self):
        print "enter B"
        super(A, self).__init__()
        print "leave B"


if __name__ == "__main__":

    B()
