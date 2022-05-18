import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline
# 프림 알고리즘을 배울 수 있었던 시간
# 기존 배운 내용은 시초가 나서 구글링으로 다른 구현 방법을 찾아봤음
# 파이썬은 객체를 함수 인자로 받아서 사용하면 객체참조가 일어나지 않는다는 점을 활용하며 배웠다.
# 함수 인자로 안받고 G로 활용하면 arr에 내용을 heappush하면 G도 같이 추가됐음
def prim(graph):
    visited[0] = 1
    arr = graph[0]
    heapq.heapify(arr)
    total = 0
    while arr:
        z, x, y = heapq.heappop(arr)
        if visited[y] == 0:
            visited[y] = 1
            total += z

            for i in G[y]:
                if visited[i[2]] == 0:
                    heapq.heappush(arr, i)
    return total

while True:
    m, n = map(int, input().split())
    ans = 0
    visited = [0] * m
    if m == 0 and n == 0:
        break
    G = defaultdict(list)
    for _ in range(n):
        x, y, z = map(int, input().split())
        G[x].append([z, x, y])
        G[y].append([z, y, x])
        ans += z
    print(ans - prim(G))
