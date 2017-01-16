
import traceback
# client
import time
import socket


def main():
    address = ('127.0.0.1', 31500)

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect(address)

            s.send('hihi')

            data = s.recv(512)
            if not data:
                print "close"
            else:
                print 'the data received is', data

        except Exception:
            print "connect or send recv"
            print str(traceback.format_exc())
        finally:
            try:
                print "close"
                s.close()
            except Exception:
                print "close_err:"
                print str(traceback.format_exc())

            time.sleep(2)


if __name__ == '__main__':
    main()
