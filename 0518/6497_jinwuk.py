import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline


def prim(graph):
    visited[0] = 1
    arr = graph[0]
    heapq.heapify(arr)
    total = 0
    while arr:
        z, x, y = heapq.heappop(arr)
        if visited[y] == 0:
            visited[y] = 1
            total += z

            for i in G[y]:
                if visited[i[2]] == 0:
                    heapq.heappush(arr, i)
    return total

while True:
    m, n = map(int, input().split())
    ans = 0
    visited = [0] * m
    if m == 0 and n == 0:
        break
    G = defaultdict(list)
    for _ in range(n):
        x, y, z = map(int, input().split())
        G[x].append([z, x, y])
        G[y].append([z, y, x])
        ans += z
    print(ans - prim(G))
