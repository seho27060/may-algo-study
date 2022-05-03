import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
def djk():
    global n, nodes

    queue = []
    heapq.heappush(queue,[0,-1,1])
    visited = [INF]*(n+1)
    visited[1] = 0
    ways = []

    while queue:
        cost, prev, now = heapq.heappop(queue)
        ways.append([prev,now])
        for node in nodes[now]:
            nxt, nxtCost = node
            if visited[nxt] > cost + nxtCost:
                visited[nxt] = cost + nxtCost
                # print(now,cost,nxt,nxtCost,visited[nxt])
                heapq.heappush(queue, [visited[nxt], now, nxt])
    # print(visited)
    return ways
n ,m = map(int,input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int,input().split())
    nodes[s].append([e,w])
    nodes[e].append([s,w])

answer = djk()
visited = [0]*(n+1)
result = []
for ans in answer[1:]:
    if not (visited[ans[0]] and visited[ans[1]]):
        result.append(ans)
        visited[ans[0]] = 1
        visited[ans[1]] = 1
print(len(result))
for res in result:
    print(*res)