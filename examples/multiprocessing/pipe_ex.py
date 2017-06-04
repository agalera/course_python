from multiprocessing import Pipe


a, b = Pipe()
a.send([1, 'hello', None])
b.recv()

b.send_bytes(b'thank you')
a.recv_bytes()
