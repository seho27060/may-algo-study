import heapq
import sys
# 다익스트라 문제
# 단방향그래프이기 때문에 역참조하는 그래프를 새로 만들어서 가는거리 오는거리를 따로 구함
# 단축방법은 생각해봐야할듯...?
input = sys.stdin.readline
def dijk(start):
    D = [1000000000] * (N+1)
    D[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dis, now = heapq.heappop(q)
        if dis > D[now]:
            continue
        for e, t in G[now]:
            if D[e] > dis + t:
                D[e] = dis + t
                heapq.heappush(q, (dis+t, e))
    return D

def dijk2(start):
    D = [1000000000] * (N+1)
    D[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dis, now = heapq.heappop(q)
        if dis > D[now]:
            continue
        for e, t in r_G[now]:
            if D[e] > dis + t:
                D[e] = dis + t
                heapq.heappush(q, (dis+t, e))
    return D
    

N, M, X = map(int, input().split())
G = [[] for _ in range(N+1)]
r_G = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    G[s].append((e, t))
    r_G[e].append((s,t))
g_root = dijk(X)
b_root = dijk2(X)
maxV = 0
for i in range(1, len(g_root)):
    if maxV < g_root[i] + b_root[i]:
        maxV = g_root[i] + b_root[i]
print(maxV)