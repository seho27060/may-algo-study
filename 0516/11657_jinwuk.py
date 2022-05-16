import sys
def func(start):
    visited[start] = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if visited[j] != INF:
                for point, num in lst[j]:
                    if visited[point] > visited[j] + num:
                        visited[point] = visited[j] + num
                        if i == N:
                            return True
    return False


INF = sys.maxsize
N, M = map(int,input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    lst[a].append([b,c])
visited = [INF]*(N+1)
if func(1):
    print(-1)
else:
    for k in range(2, N+1):
        if visited[k] == INF:
            print(-1)
        else:
            print(visited[k])
