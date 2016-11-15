import requests


class Form(object):
    """docstring for Form"""
    def __init__(self, arg):
        super(Form, self).__init__()
        self.arg = arg
        
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
