from collections import defaultdict, deque
import sys
INF = sys.maxsize
input = sys.stdin.readline

def bfs(S, E):
    V = [False] * N
    Q = deque([S])
    while Q:
        n1 = Q.popleft()

        if n1 == E:
            return True

        for t, n2 in G[n1]:
            if not V[n2]:
                Q.append(n2)
                V[n2] = True
    return False

N, S, E, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    s, e, c = map(int, input().split())
    G[s].append((c, e))
A = list(map(int, input().split()))

D = [-INF] * N
D[S] = A[S]
for i in range(N):
    for j in range(N):
        if D[j] == -INF:
            continue
        for trans, n2 in G[j]:
            if A[n2] - trans + D[j] > D[n2]:
                D[n2] = A[n2] - trans + D[j]
                if i == N-1:
                    if bfs(S, j) and bfs(j, E):
                        print('Gee')
                        exit(0)
if D[E] == -INF:
    print('gg')
else:
    print(D[E])


