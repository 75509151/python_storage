
class Subject(object):
    """docstring for Subject"""

    def __init__(self):
        self.observers = []

    def add_observer(self, obs):
        self.observers.append(obs)

    def del_observer(self, obs):
        self.observers.remove(obs)

    def notify_observer(self, *args, **kwarg):
        for obs in self.observers:
            obs.update(*args, **kwarg)


class ConcreteSubject(Subject):
    """docstring for ConcreteSubject"""

    def __init__(self):
        super(ConcreteSubject, self).__init__()

    def do_something(self, *args, **kwarg):
        self.notify_observer(*args, **kwarg)


class Observer(object):
    """docstring for ClassName"""

    def update(self, *arg, **kwarg):
        pass


class ConcreteObserver(Observer):
    """docstring for ConcreteObserver"""

    def __init__(self):
        super(ConcreteObserver, self).__init__()

    def update(self, *arg, **kwarg):
        print "recv arg:%s, kwarg:%s" % (arg, kwarg)


if __name__ == '__main__':

    obs = ConcreteObserver()
    obs2 = ConcreteObserver()
    sub = ConcreteSubject()
    sub.add_observer(obs)
    sub.add_observer(obs2)
    sub.do_something("i", "recv", {"a": "dic", "b": "dsf"}, d="heh", e="66")
