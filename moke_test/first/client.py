import requests


class Form(object):
    """docstring for Form"""

    def __init__(self):
        super(Form, self).__init__()

    def do_sell(self):
        return self.fetch_product()

    def fetch_product(self):

        print "fetch"
        return "haha"


def send_request(url):
    r = requests.get(url)
    return r.status_code


def visit_ustack():
    return send_request('http://www.ustack.com')


import os
import os.path


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)
