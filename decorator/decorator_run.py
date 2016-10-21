def fuck(fn):
    def wrap():
        print "fuck %s!" % fn.__name__[::-1].upper()
        fn()
    return wrap


def fuck_gfw(fn):
    print "fuck %s!" % fn.__name__[::-1].upper()


@fuck_gfw
def wfg():
    pass


@fuck
def hehe():
    pass


@fuck
def main():
    pass

if __name__ == '__main__':
    # wfg()
    # main()
    hehe()
