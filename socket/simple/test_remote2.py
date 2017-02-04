#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import json
import struct
import base64


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        print "Send: {}".format(message)
        sock.sendall(message)
        response = sock.recv(1024)
        # jresp = json.loads(response)
        print "Recv: ", response
        response = sock.recv(1024)
        # jresp = json.loads(response)
        print "Recv: ", response

    finally:
        sock.close()


def notify_msg(params):
    key = "kunzhi"

    plate_code = params.get("PlateCode", "闽A01001")
    pay_money = params.get("PayMoney", 1.1)
    pay_status = params.get("PayStatus", 0)

    content = {"key": key,
               "PlateCode": plate_code,
               "PayStatus": pay_status,
               "PayMone": pay_money}

    content = json.dumps(content)
    # encrypt
    content = base64.b64encode(content)
    return content


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "121.196.228.173", 8777

    msg = notify_msg({})
    client(HOST, PORT, msg)
