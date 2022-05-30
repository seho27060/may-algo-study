import sys
input = sys.stdin.readline

# 크루스칼알고리즘으로 가중치를 기반 문제를 구현하는 방식

def find(val):
    if node[val] != val:
        node[val] = find(node[val])
    return node[val]

def union(val1, val2):
    a = find(val1)
    b = find(val2)

    if a < b:
        node[b] = a
    else:
        node[a] = b

N, M = map(int, input().split())
node = [i for i in range(N+1)]
G = []
result = []
for _ in range(M):
    A, B, C = map(int, input().split())
    G.append((C, A, B))

G.sort()
for C, A, B in G:
    if find(A) != find(B):
        union(A, B)
        result.append(C)
print(sum(result[:-1]))