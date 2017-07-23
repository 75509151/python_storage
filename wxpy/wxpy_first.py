# coding: utf-8
from wxpy import *
bot = Bot()

# 机器人账号自身
myself = bot.self

my_friends = bot.friends()
print "my_friends", my_friends

send_friends_name = set([u"基本", u'宝贝'])

for f in my_friends:
    print f.name
    # if f.name in send_friends_name:
    #     f.send_msg(u"我是机器人，如果多有得罪，来咬我阿！")


everybody_groups = bot.groups().search('hi_everybody')
everybody_group = None
if everybody_groups:
    everybody_group = everybody_groups[0]
    # everybody_group.send_msg(u"我是机器人，如果多有得罪，来咬我阿！")
if everybody_group:
    menbers = []
    for menber in everybody_group:
        print menber
    print "group", everybody_group

embed()
