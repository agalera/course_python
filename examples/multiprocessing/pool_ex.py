from multiprocessing import Pool


def f(x):
    return x * x


with Pool(5) as p:
    print(p.map(f, list(range(8))))
