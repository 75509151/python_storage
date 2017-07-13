#!/usr/bin/python
#-*- coding:utf-8 -*-
import socket
import json


address = ('0.0.0.0', 65400)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
print "begin"
while True:
    try:
        data, addr = s.recvfrom(2048)

        if data:
            msg = json.loads(data)
            print msg['id'], msg['time'], msg["data"]
    except KeyboardInterrupt:
        break
    except Exception as e:
        print e
    finally:
        pass


s.close()
