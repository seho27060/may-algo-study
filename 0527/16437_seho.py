#220527 16437 양 구출 작전
# 트리 주어지는데...얼리아답터의 최소갯수..
# n <= 123,456
import sys
from collections import deque

def dfs(start):
    global n, nodes, islands, result

    cost = islands[start]
    for nxt in nodes[start]:
        cost += dfs(nxt)

    if cost < 0:
        return 0
    else:
        return cost
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
nodes = [[] for _ in range(n+1)] # i번째 노드의 부모노드/자식노드들
islands = [0]*(n+1)

for i in range(2,n+1):
    t, a, p = input().split() #동물종류, cost, 부모노드
    a, p = map(int,[a,p])
    nodes[p].append(i)
    if t == "S":
        islands[i] = a
    elif t == "W":
        islands[i] = -a
result = dfs(1)
print(result)
# 돌면서 루트노드에서 시작.
