# coding: utf-8
from wxpy import *


bot = Bot(qr_console=True)

# xiaoi = XiaoI('M3LbFZkdlujU', 'CGh8rLT0qpwIxttsmsI9')

tuling = Tuling(api_key='b59d2cb4bdc2452e811b6238bae0f80e')


@bot.register()
def reply_my_friend(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        # who = random.randint(0, 1)

        tuling.do_reply(msg)

embed()
