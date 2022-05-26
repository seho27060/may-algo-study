import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
people = [0] + list(map(int,input().split()))
road=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int, input().split())
    road[a].append(b)
    road[b].append(a)
visited=[0]*(N+1)
dp= [[0,0] for _ in range(N+1)]
result=[0,0]

def find(now):
    visited[now] = 1
    dp[now][0] = people[now]
    for i in road[now]:
        if visited[i]:
            continue
        find(i)
        dp[now][0] += dp[i][1]
        dp[now][1] += max(dp[i][0], dp[i][1])



find(1)
print(max(dp[1]))