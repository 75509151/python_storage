#!/usr/bin/python
#-*- coding:utf-8 -*-

import logging
import sys
from logging.handlers import DatagramHandler


class UdpHandler(DatagramHandler):
    """
    Send log which is already formatted to the recieve end in string format.
    """

    def __init__(self, host, port):
        DatagramHandler.__init__(self, host, port)

    def emit(self, record):
        try:
            # log_line = "%s\n" % self.format(record)
            # self.send(log_line)
            self.send("udp日志输出初始化\n")
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

if __name__ == "__main__":
    # 创建一个logger
    logger = logging.getLogger('mytest')
    logger.setLevel(logging.DEBUG)
    argv_len = len(sys.argv)
    use_arg = False if argv_len < 3 else False

    host = sys.argv[1] if use_arg else "127.0.0.1"
    port = int(sys.argv[2]) if use_arg else 65401

    # # 创建一个handler，用于写入日志文件
    # fh = logging.FileHandler('test.log')
    # fh.setLevel(logging.DEBUG)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # udp handler
    udph = UdpHandler(host, port)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    udph.setFormatter(formatter)

    # 给logger添加handler
    # logger.addHandler(fh)
    logger.addHandler(ch)

    # 记录一条日志
    logger.info('python logging test')

    logger.addHandler(udph)
    logger.info("udp log test")
