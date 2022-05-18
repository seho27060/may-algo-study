import sys
from collections import deque

## relax 하다가 사이클 발견.
## 거기서 도착점까지 bfs 실행
## 도달하면 -1 아니면 계속진행.
## 벨만포드 + 우선탐색
INF = float('inf')
input = sys.stdin.readline

def bfs(start):
    global n, nodes

    queue =deque(start)
    visited = [0]*(n+1)
    while queue:
        now = queue.popleft()
        visited[now] = 1
        for nxt, nxtCost in nodes[now]:
            if visited[nxt] == 0:
                if nxt == n:
                    return True
                queue.append(nxt)
def bf():
    global n, m, nodes, golds
    path = [-1]*(n+1)


    for i in range(n-1):
        for now in range(n):
            for nxt,nxtCost in nodes[now]:
                if golds[now] <= -INF:
                    continue
                if golds[nxt] < golds[now] + nxtCost:
                    golds[nxt] = golds[now] + nxtCost
                    path[nxt] = now

    if golds[n] <= -INF:
        print(-1)
        return
    else:
        vertices = []
        for now in range(n):
            for nxt, nxtCost in nodes[now]:
                if golds[now] <= -INF:
                    continue
                if golds[nxt] < golds[now] + nxtCost:
                    vertices.append(nxt)

        if bfs(vertices) or golds[n] <= -INF:
            print(-1)
            return
        else:
            result = [n]

            node = n
            while node != 1:
                node = path[node]
                result.append(node)
            for i in reversed(result):
                print(i, end=' ')

n, m = map(int,input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int,input().split())
    nodes[u].append([v,w])
golds = [-INF]*(n+1)
golds[1] = 0
bf()

# ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ