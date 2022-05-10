import heapq
import sys
input = sys.stdin.readline
# 다익스트라 알고리즘 문제
# 시간초과, 메모리초과, 최대값지정 등 고려할 내용이 많은문제
def dijk():
    up = [10000000000000] * (N+1)
    up[1] = 0
    q = []
    heapq.heappush(q, (up[1], 1))
    while q:
        val, now = heapq.heappop(q)
        if val != up[now]:
            continue
        for e, d in G[now]:
            if h[e] > h[now]:
                if up[e] > val + H*d:
                    up[e] = val + H*d
                    heapq.heappush(q, (up[e], e))

    down = [10000000000000] * (N+1)
    down[N] = 0
    heapq.heappush(q, (down[N], N))
    while q:
        val, now = heapq.heappop(q)
        if val != down[now]:
            continue
        for e, d in G[now]:
            if h[e] > h[now]:
                if down[e] > val + d*H:
                    down[e] = val + H*d
                    heapq.heappush(q, (down[e], e))
    ans = -10000000000000
    for i in range(2, N):
        if up[i] != 10000000000000 and down[i] != 10000000000000 and h[i] * E - up[i] - down[i] > ans:
            ans = h[i] * E - up[i] - down[i]
    if ans == -10000000000000:
        return print('Impossible')
    else:
        return print(ans)


N, M, H, E = map(int, input().split())
h = [0] + list(map(int, input().split()))
G = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    G[s].append((e, d))
    G[e].append((s, d))
dijk()