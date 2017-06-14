import socket
import struct


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1447))
text = b'hello server!'
length = len(text)

pack = struct.pack('I%ds' % length, length, text)

s.send(pack)

while True:
    s.recv(1024)
