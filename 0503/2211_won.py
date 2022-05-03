import sys
input = sys.stdin.readline
from heapq import heappush, heappop


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))

# 각 노드에서 최댓값
times = [N * 10 + 1] * (N + 1)
# 값이 갱신될 때 넣을 배열
arr = [0] * (N + 1)
qu = []
qu.append((0, 1))
times[1] = 0
while qu:
    time, curN = heappop(qu)

    # 이미 커버리면 스킵
    if times[curN] < time:
        continue

    for newTime, newN in G[curN]:
        if times[newN] > time + newTime:
            times[newN] = time + newTime
            heappush(qu, (time + newTime, newN))
            # 목표 노드로 갈 수 있는 최단 거리의 시작 노드 갱신
            arr[newN] = curN
print(N - 1)
for i in range(2, N + 1):
    print(arr[i], i)
