class Observable:

    def __init__(self, initialValue=None):

        self._data = initialValue

        self.callbacks = {}

    def addCallback(self, func):

        self.callbacks[func] = 1

    def delCallback(self, func):

        del self.callback[func]

    def _docallbacks(self):

        for func in self.callbacks:

            func(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        print "hehe"
        self._docallbacks()


def money_change(data):
    print "now money: %s" % data


if __name__ == '__main__':
    money = Observable(3)
    money.addCallback(money_change)
    money.data = 6
    print money.data
