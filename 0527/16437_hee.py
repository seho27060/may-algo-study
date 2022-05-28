import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

def dfs(n1):
    global ans
    V[n1] = True
    D[n1] = S[n1] - W[n1]
    for n2 in G[n1]:
        if not V[n2]:
            dfs(n2)
            D[n1] += max(D[n2], 0)

N = int(input())
G = [[] for _ in range(N+1)]
W = [0] * (N+1)
S = [0] * (N+1)
for i in range(2, N+1):
    t, a, p = map(str, input().split())
    if t == 'W':
        W[i] += int(a)
    else:
        S[i] += int(a)
    G[i].append(int(p))
    G[int(p)].append(i)

V = [False] * (N+1)
D = [0] * (N+1)
dfs(1)
print(D[1])