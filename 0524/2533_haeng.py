import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
road=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int, input().split())
    road[a].append(b)
    road[b].append(a)

dp= [0]*(N+1)
visited=[0]*(N+1)
result=0

def find(p,now):
    global result
    visited[now] = 1

    cnt = 0
    for i in road[now]:
        if visited[i]:
            continue
        find(now,i)

        cnt +=2
    if cnt == 0:
        dp[p] += 1
        return
    if dp[now] < cnt:
        dp[p] += 2
        result += 1

find(0,1)
print(result)