import heapq
import sys
input = sys.stdin.readline
# 다익스트라의 2차원 배열 문제
# 힙큐에 넣는 순서에 따라 시간순서가 크게 바뀌니 명심하고 문제풀어야함!
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dijk():
    visited = [[1000000000] * (N) for _ in range(N)]
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    visited[0][0] = arr[0][0]
    while q:
        val, y, x = heapq.heappop(q)
        if val > visited[N-1][N-1]:
            continue
        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] > val + arr[ny][nx]:
                visited[ny][nx] = val + arr[ny][nx]
                heapq.heappush(q, (visited[ny][nx], ny, nx))
    return visited[N-1][N-1]

cnt = 1
while True:
    N = int(input())
    if N == 0:
        exit()
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {cnt}: {dijk()}')
    cnt += 1