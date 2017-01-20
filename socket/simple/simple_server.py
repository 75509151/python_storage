# server

import socket
import json
import time

address = ('127.0.0.1', 55555)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
s.bind(address)
s.listen(5)

while True:
    ss, addr = s.accept()
    if ss:
        print 'got connected from', addr
        ra = ss.recv(512)
        json.loads(ra)
        ss.send('byebye')
        print ra
        ss.close()
        ss = None
    else:
        time.sleep(1)
s.close()
