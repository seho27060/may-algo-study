import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(n1):
    V[n1] = True
    D[n1][1] = A[n1]

    for n2 in G[n1]:
        if not V[n2]:
            dfs(n2)
            D[n1][1] += D[n2][0]
            D[n1][0] += max(D[n2][0], D[n2][1])

N = int(input())
A = [0] + list(map(int, input().split()))
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

V = [False] * (N+1)
D = [[0, 0] for _ in range(N+1)]
dfs(1)
print(max(D[1][1], D[1][0]))
