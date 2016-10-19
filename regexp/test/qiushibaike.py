# coding: utf-8
# 段子的发布人，发布日期，内容以及点赞个数。
import re

auther_pattern = r'<div.*?class="author.*?<a.*?<a.*?title=(.*?)>'
content_pattern = r'<div.*?class="content">.*?<span>(.*?)</span>'
vote_pattern = r'class="stats-vote"><i class="number">(.*?)<'
pattern = r'<div.*?class="author.*?<a.*?<a.*?title=(.*?)>.*?<div.*?class="content">.*?<span>(.*?)</span>' + r".*?" + vote_pattern

with open("/home/mm/code_dept/python/reg/test/qiushibaike.html", "r") as f:
    web_content = f.read()
    # print web_content
    # items = re.findall(content_pattern, web_content, re.S)
    # for item in items:
    #     print "content: %s" % item
    # authers = re.findall(auther_pattern, web_content, re.S)

    # for auther in authers:
    #     print "auther: %s" % auther
    # votes = re.search(vote_pattern, web_content, re.S)
    # if votes:
    #     print votes.group(0)
    items = re.findall(pattern, web_content, re.S)
    for item in items:
        print "auther:%s\n content:%s\n vote:%s\n\n" % (item[0], item[1], item[2])
