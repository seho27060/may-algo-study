from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline

def prim():
    V = [False] * n
    Q = [(0, 0)]
    temp = 0
    while Q:
        c, n1 = heappop(Q)

        if V[n1]:
            continue

        V[n1] = True
        temp += c

        for c, n2 in G[n1]:
            if not V[n2]:
                heappush(Q, (c, n2))
    return temp

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    G = defaultdict(list)
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        G[x].append((z, y))
        G[y].append((z, x))
        total += z
    print(total - prim())