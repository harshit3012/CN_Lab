class Topology:
    def __init__(self, n):
        self.matrix = []
        self.n = n

    def addlink(self, u, v, w):
        self.matrix.append((u, v, w))

    def table(self, dist, src):
        print("Vector Table of {}".format(chr(ord('A')+src)))
        print("Dest\tcost")

        for i in range(self.n):
            print("{0}\t{1}".format(chr(ord('A')+i), dist[i]))

    def bellmanford(self, src):
        dist = [9999] * self.n
        dist[src] = 0

        for _ in range(self.n - 1):
            for u, v, w in self.matrix:
                if dist[u] != 9999 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        self.table(dist, src)


def main():
    matrix = []
    n = int(input("Enter number of Nodes : "))
    print("Enter the Adjacency Matrix :")
    for i in range(n):
        m = list(map(int, input().strip().split()))
        matrix.append(m)
    topo = Topology(n)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                topo.addlink(i, j, 1)

    for a in range(n):
        topo.bellmanford(a)


main()
