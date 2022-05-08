import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
def dfs(start):
    global n, end, nodes
    visited = [0]*n
    stack = [start]
    while stack:
        now = stack.pop()
        if now == end:
            return True
        visited[now] = 1
        for nxt, cost in nodes[now]:
            if visited[nxt] == 0:
                stack.append(nxt)
    return False

def Belman():
    global end, dst, n
    for i in range(n+1):
        if dst[end] == -INF and i == n:
            print('gg')
            return
        for j in range(n):
            if dst[j] == -INF:
                continue
            for nxt, cost in nodes[j]:
                if dst[j] + cost > dst[nxt]:
                    dst[nxt] = dst[j] + cost
                    if i == n:
                        if dfs(nxt):
                            print('Gee')
                            return False
    return True
# start에서 end를 가는데, 비용 최댃값 구하기.
# 각 도시(노드) 도착하면 수익이 발생. 간선타면 비용 발생.
# 도착불가시 gg, 도착했는데 비용이 무한대라면 Gee 출력.
n, start, end, m = map(int,input().split())
# n,m <= 50/ w <= 백만, 음이 아닌 정수.
nodes = [[] for _ in range(n)]

for _ in range(m):
    s, e, w = map(int,input().split())
    nodes[s].append([e,w])

cities = list(map(int,input().split())) # 도시도착하면 발생 수익
dst = [-INF]*(n)

dst[start] = cities[start]
# print(dst)
# n*m 사이클 체크해서
# 한번더 했는데 값 변경이 일어났다. -> Gee
# 없는데 값이 -1이다. -> gg
# 위 사항이 아니다 -> 값출력
# cities는 음수로, 간선비용은 양수로 비교
# 이동할때마다 더 작은 값이면 갱신(부호 역전이므로 결국 최대값이 갱신됨.#
# 갱신 -> 사이클 노드.
# bfs로 경로 찾으면서 경로에 사이클 노드있을시, Gee
# 없다면
for i in range(n):
    for j in range(len(nodes[i])):
        for k in range(n):
            if nodes[i][j][0] == k:
                nodes[i][j][1] = cities[k] - nodes[i][j][1]

if Belman():
    print(dst[end])