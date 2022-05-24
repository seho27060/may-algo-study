from collections import defaultdict
# defaultdict 쓰면 메모리 초과남
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(n1):
    V[n1] = True
    D[n1][1] = 1
    for n2 in G[n1]:
        if not V[n2]:
            dfs(n2)
            D[n1][1] += min(D[n2][0], D[n2][1])
            D[n1][0] += D[n2][1]

N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

D = [[0, 0] for _ in range(N+1)]
V = [False] * (N+1)
dfs(1)
print(min(D[1][0], D[1][1]))



