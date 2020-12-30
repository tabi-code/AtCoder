
class Lca(object):
    def __init__(self, graph, root=0):
        self.graph = graph
        self.root = root
        self.n = len(graph)
        self.bit_len = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.bit_len)]
        self.bfs()
        self.doubling()

    def bfs(self):
        ql = [[0, self.root]]
        ql = collections.deque(ql)
        fq = collections.defaultdict(list)
        fq[self.root] = 0
        while True:
            if len(ql) != 0:
                cost, tmp = ql.popleft()
                for tmv in self.graph[tmp]:
                    if tmv not in fq:
                        ql.append([cost + 1, tmv])
                        fq[tmv] = cost + 1
            else:
                break

    def doubling(self):
        for i in range(1, self.bit_len):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

    def get(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        du = self.depth[u]
        dv = self.depth[v]

        for i in range(self.bit_len):
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        if u == v:
            return u

        for i in range(self.bit_len - 1, -1, -1):
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]