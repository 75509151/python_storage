import socket
import time

LEN = 500000

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 65530))
    print "c"
    date = "1" * LEN
    i = 0
    while True:
        sock.sendall(date)
        print i
        i+=1
        time.sleep(2)
