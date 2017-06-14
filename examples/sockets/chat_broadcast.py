from socket import *
import traceback
from threading import Thread


class broadcast_recv(Thread):
    def __init__(self, cs):
        Thread.__init__(self)
        self.s = cs
        self.s.bind(('', 51423))

    def run(self):
        while True:
            try:
                message, address = self.s.recvfrom(1024)
                print(">", address[0], "->", message)
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                traceback.print_exc()


cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

t1 = broadcast_recv(cs)
t1.start()

while True:
    text_introduced = input('')
    cs.sendto(text_introduced.encode('ascii'),
              ('255.255.255.255', 51423))
