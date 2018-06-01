# coding: utf-8
from wxpy import *

bot = Bot()
my_friend = ensure_one(bot.search(u'陈若晨'))
xiaoi = XiaoI('M3LbFZkdlujU', 'CGh8rLT0qpwIxttsmsI9')


@bot.register()
def reply_my_friend(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        xiaoi.do_reply(msg)

embed()
