import socket

address = ('192.168.2.211', 554)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = s.recv(100)
    if not msg:
        break
    print msg

s.close()
print "over"
