#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import json
import struct
import errno
from socket import error as socket_error


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        print "Send: {}".format(message)
        sock.sendall(message)
        # sock.close()
        response = sock.recv(1024)
        # jresp = json.loads(response)
        print "Recv: ", response
    except socket_error as serr:
        if serr.errno != errno.ECONNREFUSED:
            print "connect error"

    finally:
        sock.close()


def notify_msg(params):
    key = "kunzhi"

    plate_code = params.get("PlateCode", "闽A00001")
    pay_money = params.get("PayMoney", 1.1)
    pay_status = params.get("PayStatus", 1)

    content = {"key": key,
               "PlateCode": plate_code,
               "PayStatus": pay_status,
               "PayMoney": pay_money}

    content = json.dumps(content)
    # encrypt
    return content


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "121.196.228.173", 8777

    msg = notify_msg({})
    client(HOST, PORT, msg)
