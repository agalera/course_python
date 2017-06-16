import socket
import struct
import hashlib

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('0.0.0.0', 1448))

serversocket.listen(5)


socket, addr = serversocket.accept()


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def recv(socket, length):
    package = b""
    while True:
        p1 = socket.recv(length - len(package))
        if not p1:
            raise Exception("disconnect user")
        package += p1
        if len(package) == length:
            return package


def read_messages(socket):
    r = recv(socket, 4)
    length = struct.unpack('I', r)[0]
    r = recv(socket, length)
    return struct.unpack('%ds' % length, r)[0]


def get_file(socket, filename):
    f = open(filename, 'wb')
    r = recv(socket, 4)
    length = struct.unpack('I', r)[0]
    chunks = length // 1024
    resto = length % 1024
    for chunk in range(chunks):
        f.write(socket.recv(1024))
    f.write(socket.recv(resto))
    f.close()

    print("ok")
    r = recv(socket, 4)
    length = struct.unpack('I', r)[0]
    r = recv(socket, length)
    r = struct.unpack('%ds' % length, r)[0].decode('ascii')
    print(r, md5(filename))
    if r == md5(filename):
        print("md5 ok")
    else:
        print("md5 error")

get_file(socket, "prueba.mp4")
