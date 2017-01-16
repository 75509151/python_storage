# server

import socket

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
s.bind(address)
s.listen(5)

while True:
    ss, addr = s.accept()
    print 'got connected from', addr

    ra = ss.recv(512)
    ss.send('byebye')
    print ra
    ss.close()
s.close()
