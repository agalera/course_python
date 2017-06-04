from multiprocessing import Process, Manager


def worker(n, share_dict):
    for x in range(10):
        share_dict["%s_%s" % (n, x)] = x


share_dict = Manager().dict()

threads = []
for x in range(2):
    threads.append(Process(target=worker, args=(x, share_dict, )))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(share_dict.keys())
