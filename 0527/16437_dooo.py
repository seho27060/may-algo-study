import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(now):
    ans = 0
    for i in G[now]:
        ans += dfs(i)
    if v[now][0] == 'S' and now != 1:
        ans += v[now][1]
    elif v[now][0] == 'W':
        ans -= v[now][1]
    if ans <= 0:
        ans = 0
    return ans
n = int(input())
G = [[] for _ in range(n+1)]
v = [[], [0,0]]
for i in range(n-1):
    a, b, c = map(str, input().split())
    G[int(c)].append(i+2)
    v.append((a, int(b)))
print(dfs(1))