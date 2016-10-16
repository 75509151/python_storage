# coding: utf-8
import urllib2
import re
import os
import cookielib
import logging
import logging.config
# log

logging.config.fileConfig("../spider_log.conf")  # 采用配置文件
log = logging.getLogger('spider')
log.setLevel(logging.DEBUG)
# save_file
save_file = os.path.join("/home/mm/code_depot/python/spider/first/", "qiushibaike.html")

# request
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
headers = {'User-Agent': user_agent}


# build opener
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
# build request
first_url = "http://www.qiushibaike.com/hot/"

pattern = re.compile('div')
f = open(save_file, "w+")
for i in range(1):
    url = first_url + str(i)
    request = urllib2.Request(url, headers=headers)
    try:
        response = opener.open(request)
        # print response.read()
        content = response.read()

        f.write(content)
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            log.info(e.code)
        if hasattr(e, 'reason'):
            log.info(e.reason)
