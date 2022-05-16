### 220516 11657 타임머신

# n개 도시,m개 간선(500,6000) a, b, c = s,e,w
# 음수 가중치 있음
# 음수사이클이 있다면 -1 출력
# 아니라면 각 도시까지 걸리는 시간 낮은 순서대로 출력. 경로가 없다면 -1 출력
import sys
INF = sys.maxsize
input = sys.stdin.readline

def bf():
    global n, m, ways, times
    cycle = False
    for N in range(n+1):
        for M in range(m):
            s, e, w = ways[M]
            if times[s] >= INF:
                continue
            if times[e] > times[s] + w:
                times[e] = times[s] + w
                if N == n:
                    return print(-1)
    for time in times[2:]:
        if time < INF:
            print(time)
        else:
            print(-1)
n, m = map(int,input().split())
ways = []
for _ in range(m):
    a, b, c = map(int,input().split())
    ways.append([a,b,c])

times = [INF]*(n+1)
times[1] = 0

bf()