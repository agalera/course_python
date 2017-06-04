iterable = {'blue': 5, 'green': 2, 'red': 10}

# convert all values to string
a = {k: str(iterable[k]) for k in iterable}
b = {k: iterable[k] if iterable[k] % 2 else 0 for k in iterable}
c = {k: iterable[k] for k in iterable if k in ['blue', 'red']}
