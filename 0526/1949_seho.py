#220526 1949 우수 마을
# 트리 구조, 양방향 그래프
# 우수마을끼리ㄴ는 인접할 수가없다.
# 안 우수마을은 최소 1개의 우수마을과 인접..
# 최대의 우수마을의 주민수 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(start):
    global visited, dp, trees

    visited[start] = 1
    for nxt in trees[start]:
        if not visited[nxt]:
            dfs(nxt)
            dp[start][1] += dp[nxt][0]
            dp[start][0] += max(dp[nxt][0], dp[nxt][1])

n = int(input())
citizens = [0]
citizens += list(map(int,input().split()))
dp = [[0, citizens[i]]*2 for i in range(n+1)]
visited = [0]*(n+1)

trees = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int,input().split())
    trees[s].append(e)
    trees[e].append(s)

dfs(1)
print(max(dp[1][1], dp[1][0]))