class LoginUser(object):
    """docstring for LoginUser"""

    def __init__(self):
        super(LoginUser, self).__init__()
        self._name = ""
        self._psw = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        print "set name"

    @property
    def psw(self):
        return self._psw

    @psw.setter
    def psw(self, value):
        self._psw = value

    def check(self):
        if self._name == "admin" and self._psw == "123456":
            return True
        else:
            return False


if __name__ == '__main__':
    u = LoginUser()
    u.name = "jay"
    print u.name
    print u.psw
