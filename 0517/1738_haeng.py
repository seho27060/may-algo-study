import sys
input = sys.stdin.readline

def check(x2):
    visited = [False]*(n+1)
    ST=[x2]
    while ST:
        node = ST.pop(0)
        if node == n:
            return True
        visited[node] = True

        for k in road:
            if k[0] == node and visited[k[1]] == False:
                ST.append(k[1])
    return False


def bfs(n):         #역으로 경로탐색
    ST = [n]
    result2=[-9999999999999]*(n+1)
    result2[n] = 0
    route=[[] for _ in range(n+1)]
    route[n]=[n]

    while ST:
        now = ST.pop(0)
        if now == 1 and result2[1]==result[n]:
            return reversed(route[1])


        for k in road:
            if k[1] == now and result2[k[0]] < result2[now]+k[2]:
                ST.append(k[0])
                result2[k[0]]= result2[now]+k[2]
                route[k[0]] = route[k[1]] + [k[0]]


def bf():
    for i in range(n):
        for now,next,cost in road:
            if result[now] != -9999999999999 and result[next] < result[now]+cost:
                result[next] = result[now]+cost
                if i == n-1 and check(next):
                    return True

    return False



n,m = map(int,input().split())

road = []
for _ in range(m):
    road.append(list(map(int,input().split())))

result = [-9999999999999] * (n+1)
result[1] = 0

if bf():
    print(-1)
else:
    if result[n] == -9999999999999:
        print(-1)
    else:
        print(*bfs(n))