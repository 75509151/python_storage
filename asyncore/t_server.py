import asyncore
import socket
import traceback
import sys
from errno import EALREADY, EINPROGRESS, EWOULDBLOCK, ECONNRESET, EINVAL, \
        ENOTCONN, ESHUTDOWN, EINTR, EISCONN, EBADF, ECONNABORTED, EPIPE, EAGAIN, \
        errorcode
_DISCONNECTED = frozenset((ECONNRESET, ENOTCONN, ESHUTDOWN, ECONNABORTED, EPIPE,
                                                   EBADF))


LEN = 500000


class FixDispather(asyncore.dispatcher):
    def __init__(self, sock=None, map=None):
        asyncore.dispatcher.__init__(self, sock, map)

    def recv(self, buffer_size):
        try:
            data = self.socket.recv(buffer_size)
            if not data:
                # a closed connection is indicated by signaling
                # a read condition, and having recv() return 0.
                self.handle_close()
                return ''
            else:
                return data
        except socket.error, why:
            # winsock sometimes throws ENOTCONN
            if why.args[0] in _DISCONNECTED:
                self.handle_close()
                return ''
            elif why.args[0] in (EAGAIN, EWOULDBLOCK):
                return ''
            else:
                raise


class Client(FixDispather):
    def __init__(self, sock):
        FixDispather.__init__(self, sock)
        self.sock = sock
        self.handle_read = self.read_while
        self.i = 0

    def handle_error(self):
        traceback.print_exc()
        print "e: %s" % self.sock

    def handle_close(self):
        print "close: %s" % self.sock
        try:
            self.close()
        except:
            traceback.print_exc()

    def read_while(self):
        data = self.recv(1)
        while len(data) < LEN and data:
            data += self.recv(LEN - len(data))
        if not len(data) == LEN:
            print "Warning: recv not %s" % LEN
            raise RuntimeError("not %s" % LEN)
        print "len: %s, %s" % (len(data), self.i)
        self.i += 1


class EchoServer(FixDispather):

    def __init__(self, host, port):
        FixDispather.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        print "bind"
        self.listen(5)

    def handle_accept(self):
        client_info = self.accept()
        if client_info is not None:
            print 'Incoming connection from: %s' % str(client_info)
            handler = Client(client_info[0])


if __name__ == "__main__":
    server = EchoServer('localhost', 65530)
    asyncore.loop()
