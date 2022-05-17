
import sys
input = sys.stdin.readline
INF = sys.maxsize
from collections import defaultdict


def check(v):
    Q = [v]
    visit = set()
    visit.add(v)

    while Q:
        curV = Q.pop(0)
        if curV == n: return True

        for neiV in adj[curV]:
            if neiV not in visit:
                Q.append(neiV)
                visit.add(neiV)

    return False


def bellmanFord():
    dist = [-INF for _ in range(n + 1)]  # 0, 1 ~ n
    dist[1] = 0

    nodes = defaultdict(int)

    for _ in range(n - 1):
        tmp = dist.copy()

        for start, end, cost in edges:
            if dist[start] == -INF: continue
            if tmp[end] < dist[start] + cost:
                tmp[end] = dist[start] + cost
                # nodes[end] = start
                # print(start, end)
                # start는 분기가 너무 많아서 반대로 end로 바꿔보았다
                # 목적지를 선택하는 것 우선 (반대로 선택해 나가도록)
                nodes[end] = start

        dist = tmp

    if dist[n] == -INF:
        return -1

    for start, end, cost in edges:
        if dist[start] == -INF: continue
        if dist[end] < dist[start] + cost:
            if check(end):
                return -1

    return nodes


n, m = map(int, input().split())
edges = []
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    adj[a].append(b)

ans = bellmanFord()

if ans == -1: print(-1)
else:
    num = n  # 1부터가 아니라 n부터 반대로 타고 내려가기
    res = [n]
    while num != 1:
        num = ans[num]
        res.append(num)
    res.reverse()
    print(*res)