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
logging.addLevelName(logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
# save_file
save_file = os.path.join("/home/mm/code_dept/python/spider/first/", "qiushibaike.html")

# request
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
headers = {'User-Agent': user_agent}


# build opener
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
# build request
base_url = "http://www.qiushibaike.com/hot/"

auther_pattern = r'<div.*?class="author.*?<a.*?<a.*?title=(.*?)>'
content_pattern = r'<div.*?class="content">.*?<span>(.*?)</span>'
vote_pattern = r'class="stats-vote"><i class="number">(.*?)<'
pattern = r'<div.*?class="author.*?<a.*?<a.*?title=(.*?)>.*?<div.*?class="content">.*?<span>(.*?)</span>' + r".*?" + vote_pattern

f = open(save_file, "w+")
for i in range(1):
    url = base_url + str(i)
    request = urllib2.Request(url, headers=headers)
    try:
        response = opener.open(request)
        # print response.read()
        log.WARNING("hehe")
        web_content = response.read()
        # f.write(response.read())
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            log.info(e.code)
        if hasattr(e, 'reason'):
            log.info(e.reason)
