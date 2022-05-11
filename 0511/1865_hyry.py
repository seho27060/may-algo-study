
import sys
input = sys.stdin.readline


def bellmanFord(start):
    D = [1e10] * (V + 1)
    D[start] = 0

    for _ in range(V - 1):
        tmp = D.copy()
        for s, e, c in edges:
            if D[s] + c < tmp[e]:
                tmp[e] = D[s] + c
        D = tmp

    for s, e, c in edges:
        if D[s] == 1e10: continue
        if D[s] + c < D[e]: return True

    return False


T = int(input())
for _ in range(T):
    V, E, W = map(int, input().split())
    edges = []
    for _ in range(E):
        v1, v2, c = map(int, input().split())
        edges.append((v1, v2, c))
        edges.append((v2, v1, c))

    for _ in range(W):
        v1, v2, c = map(int, input().split())
        edges.append((v1, v2, -c))

    if bellmanFord(1): print("YES")
    else: print("NO")
