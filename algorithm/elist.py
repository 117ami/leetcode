import bisect


class Elist:
    def __init__(self, size=1):
        self.data = list(range(size))
        self.parent = {i: i for i in range(1 + len(self.data))}
        self.indexes = {n: i for i, n in enumerate(self.data)}
        # print(self.indexes)

    def find(self, i):
        if self.parent[i] != i:
            j = self.find(self.parent[i])
            self.parent[i] = j
        return self.parent[i]

    def merge(self, i):
        self.parent[i] = i + 1

    def remove(self, n):
        idx = self.indexes[n]
        if idx == self.find(idx):
            self.merge(idx)


import random
N = 50000


def a():
    l = Elist(N)
    # print(l.data)
    for i in range(N // 2):
        n = random.randint(0, N - 1)
        # print(n)
        l.remove(n)


# print(l.parent)
def b():
    l = list(range(N))
    # print(l.data)
    m = N - 1
    for i in range(N // 2):
        n = random.randint(0, m)
        # print(n)
        del l[n]
        m -= 1


import timeit
number = 100
print(timeit.timeit(a, setup="from __main__ import a", number=number))
print(timeit.timeit(b, setup="from __main__ import b", number=number))
