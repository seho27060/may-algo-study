# 단뱡항.
# n = 1000 m = 10000
# n개의 시작점에서 x번으로 이동하고 다시 각 n번으로 돌아갈때
# 가장 오래걸리는 마을 찾기.
# i-x 로 n개의 다익스트라 최단경로 구하기
# 각 경로에서 x까지 경로길이 구하고. x-i에서 x에서 i까지 경로 구해서 두개 더해주면
# 시작점 i에서 n을 찍고 다시 i로 돌아오는 경로
# n개의 찍턴 경로가 나오고 거기중 가장 큰 값 비교.
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def djk(start):
    global nodes, n, x

    visited = [INF]*(n+1)
    visited[start] = 0

    queue = []
    heapq.heappush(queue,[0,start])

    while queue:
        cost, now = heapq.heappop(queue)
        for node in nodes[now]:
            nxt, nxtCost = node
            if visited[nxt] > cost + nxtCost:
                visited[nxt] = cost + nxtCost
                heapq.heappush(queue,[visited[nxt],nxt])
    return visited

n, m, x = map(int,input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int,input().split())
    nodes[s].append([e,w])

wayBackHome = [ [] for _ in range(n+1)]
for start in range(1,n+1):
    wayBackHome[start]= djk(start)

answer = [0]*(n+1)

for start in range(1,n+1):
    answer[start] = wayBackHome[start][x] + wayBackHome[x][start]
print(max(answer[1:]))