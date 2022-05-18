import sys

def func():
    money[1] =0
    for i in range(N):
        for j in range(1,N+1):
            for point, num in lst[j]:
                if money[j] == INF:
                    continue

                elif money[point] < money[j] + num:
                    money[point] = money[j]+num
                    visited[point] = j

                    if i == N-1:
                        money[point] = -INF





INF = -sys.maxsize
N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
visited = [0]*(N+1)
money = [INF] * (N+1)
for _ in range(M):
    U,V,W = map(int,input().split())
    lst[U].append([V,W])

result = []
func()

if money[N] == -INF:
    print(-1)
else:
    result.append(N)

    while True:
        N = visited[N]
        result.append(N)
        if N == 1:
            break
    for i in range(len(result)-1, -1, -1):
        print(result[i], end=" ")
    print()