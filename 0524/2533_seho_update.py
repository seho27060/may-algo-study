#220524 2533 사회망 서비스(SNS)
# 트리 주어지는데...얼리아답터의 최소갯수..
# n <= 1,000,000
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(s):
    global n, trees, dp, visited

    visited[s] = 1
    dp[s][0] = 1

    for tree in trees[s]:
        if visited[tree] == 0:
            dfs(tree)
            dp[s][0] += min(dp[tree][0], dp[tree][1])
            dp[s][1] += dp[tree][0]
n = int(input())
trees = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int,input().split())
    trees[u].append(v)
    trees[v].append(u)
visited = [0]*(n+1)
dp = [[0,0] for _ in range(n+1)]
dfs(1)
print(min(dp[1]))