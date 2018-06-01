#coding:utf-8
from wxpy import *

# 初始化机器人
bot = Bot()
# 找到需要接收日志的群 -- `ensure_one()` 用于确保找到的结果是唯一的，避免发错地方
group_receiver = ensure_one(bot.groups().search('hi_everybody'))

# 指定这个群为接收者
logger = get_wechat_logger(group_receiver)

logger.error(u'打扰大家了，但这是一条重要的错误日志...')
