import sys
import collections
INF = sys.maxsize

def bf():
    r = collections.defaultdict(int)
    for i in range(n):
        for j in range(1, n+1):
            if money[j] == -INF:
                continue
            for v, w in graph[j]:
                if money[v] < money[j]+w:
                    money[v] = money[j]+w
                    r[v] = j
                    if i == n-1:
                        money[v] = INF
                        if v == n:
                            print(-1)
                            return

    p = r[n]
    visit = []
    visit.append(n)
    while p != 1:
        visit.insert(0, p)
        p = r[p]
    visit.insert(0, 1)
    print(*visit)
    return

n, m = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
money = [-INF] * (n+1)
money[1] = 0

bf()