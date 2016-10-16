# -*- coding: UTF-8 -*-

import urllib2
import cookielib
# cookielib模块的主要作用是提供可存储cookie的对象，
# 以便于与urllib2模块配合使用来访问Internet资源。Cookielib模块非常强大，我们可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，比如可以实现模拟登录功能。该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。

# 它们的关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar

cookie = cookielib.CookieJar()
# save cookie in variable
cookieHandler = urllib2.HTTPCookieProcessor(cookie)
httpHandler = urllib2.HTTPHandler()

opener = urllib2.build_opener(cookieHandler, httpHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen("http://www.baidu.com")
for item in cookie:
    print "name: %s, value: %s" % (item.name, item.value)


file_name = "cookie.txt"
cookie = cookielib.MozillaCookieJar(file_name)
# save cookie in file
cookieHandler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookieHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)

cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)

request = urllib2.Request("http://www.baidu.com")
response = opener.open(request)
print response.read()
