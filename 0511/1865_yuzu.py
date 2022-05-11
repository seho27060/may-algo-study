import sys
import collections
INF = sys.maxsize

def bf():
    time = [INF] * (n+1)
    time[1] = 0
    for i in range(n):
        for j in range(1, n+1):
            for e, t in graph[j]:
                if time[e] > time[j]+t:
                    time[e] = time[j]+t
                    if i == n-1:
                        return True
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())

    graph = collections.defaultdict(list)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    if bf():
        print('YES')
    else:
        print('NO')