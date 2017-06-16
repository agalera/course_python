from multiprocessing import (Pool, BoundedSemaphore,
                             cpu_count, current_process)
import requests


sem = BoundedSemaphore(200)

r = requests.get('http://firecarrot.com:9000').json()['result']


def f(url):
    print(current_process(), url)

    with sem:
        return requests.get(url).json()['result']


p = Pool(cpu_count() * 10)


result = p.map(f, r)
print(sum(result))
