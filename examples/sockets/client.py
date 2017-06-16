import socket
import struct
import os
import hashlib


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_size(f):
    return os.fstat(f.fileno()).st_size


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1448))

f = open('file.mp4', 'rb')
length = get_size(f)
pack = struct.pack('I', length)
s.send(pack)

chunks = length // 1024
resto = length % 1024

for n in range(chunks):
    print("send chunk", n)
    s.send(f.read(1024))
s.send(f.read(resto))
hash_md5 = md5("file.mp4")
length = len(hash_md5)
p = struct.pack('I%ds' % length, length, hash_md5.encode('ascii'))
s.send(p)
