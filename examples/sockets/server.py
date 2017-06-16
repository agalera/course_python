import socket
from threading import Thread
import struct


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('0.0.0.0', 1447))

serversocket.listen(5)


class Client(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.sock = sock

    def recv(self):
        r = self.sock.recv(4)
        if not r:
            return False
        length = struct.unpack('I', r)[0]
        package = self.sock.recv(length)
        return struct.unpack('%ds' % length, package)[0]

    def recv3(self, length):
        package = b""
        while True:
            p1 = self.sock.recv(length - len(package))
            if not p1:
                raise Exception("disconnect user")
            package += p1
            if len(package) == length:
                return package

    def recv2(self):
        r = self.sock.recv(4)
        if not r:
            return False
        length = struct.unpack('I', r)[0]

    def run(self):
        while True:
            r = self.recv()
            if r is False:
                print("disconnect")
                break
            print(r)


while True:
    (sock, address) = serversocket.accept()
    Client(sock).start()
