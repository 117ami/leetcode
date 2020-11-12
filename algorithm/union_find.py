class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def merge(self, x, y):
        # Merge by size of set
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self.size[px] < self.size[py]:
            self.p[px] = py
            self.size[py] += self.size[px]
        else:
            self.p[py] = px
            self.size[px] += self.size[py]

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

