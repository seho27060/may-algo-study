# n*n bfs? 최소비용 구하기? -> djk보다 느림. 해결가능.
# djk ->
# n = 125
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def djk():
    global n, board

    visited = [[INF]*n for _ in range(n)]
    visited[0][0] = board[0][0]

    moves = [[0,1],[0,-1],[1,0],[-1,0]]

    queue = []
    heapq.heappush(queue,[board[0][0],[0,0]])

    while queue:
        cost, now= heapq.heappop(queue)
        for move in moves:
            nxtR = now[0] + move[0]
            nxtC = now[1] + move[1]
            if 0 <= nxtR < n and 0 <= nxtC < n:
                if visited[nxtR][nxtC] > cost + board[nxtR][nxtC]:
                    visited[nxtR][nxtC] = cost + board[nxtR][nxtC]
                    heapq.heappush(queue,[visited[nxtR][nxtC],[nxtR,nxtC]])
    return visited

tc = 0
while 1:
    tc += 1
    n = int(input())
    if n == 0:
        break

    board = [list(map(int,input().split())) for _ in range(n)]

    answer = djk()
    print(f"Problem {tc}: {answer[n-1][n-1]}")