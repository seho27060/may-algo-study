import heapq
import sys
input = sys.stdin.readline

def dijkstra(t):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = [(arr[0][0], [0, 0])]
    visit = [[0]*n for _ in range(n)]
    visit[0][0] = 1
    cost = [[1e9]*n for _ in range(n)]
    cost[0][0] = arr[0][0]
    while q:
        k, node = heapq.heappop(q)
        if cost[node[0]][node[1]] < k:
            continue
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if 0<=nx<n and 0<=ny<n and k+arr[nx][ny] < cost[nx][ny] and visit[nx][ny] == 0:
                cost[nx][ny] = k+arr[nx][ny]
                visit[nx][ny] = 1
                heapq.heappush(q, (k+arr[nx][ny], [nx, ny]))
    print(f'Problem {t}:', cost[-1][-1])
    return

t = 0
while True:
    t += 1
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    dijkstra(t)