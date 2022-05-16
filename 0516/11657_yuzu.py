import sys
import collections
INF = sys.maxsize

def bf():
    for i in range(n):
        for j in range(1, n+1):
            if time[j] == INF:
                continue
            for e, t in graph[j]:
                if time[e] > time[j]+t:
                    time[e] = time[j]+t
                    if i == n-1:
                        return False
    return True

n, m= map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
time = [INF] * (n+1)
time[1] = 0
if bf():
    for t in time[2:]:
        if t != INF:
            print(t)
        else:
            print(-1)
else:
    print(-1)