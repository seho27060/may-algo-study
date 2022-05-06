
import sys
input = sys.stdin.readline


def check(start):

    Q = [start]
    visited = [False] * N
    visited[start] = True

    while Q:
        curV = Q.pop(0)
        if curV == end: return True

        for neiV in adj[curV]:
            if not visited[neiV]:
                Q.append(neiV)
                visited[neiV] = True

    return False


def bellmanFord():

    memo = [-1e10] * N  # 최소가 아닌 최대를 구해야 하니 -Infinity
    memo[start] = income[start]

    # 1. 최단거리는
    #    노드들이 한 줄로 이어져 아무리 길어도 N - 1을 벗어날 수 없다
    for _ in range(N - 1):
        tmp = memo.copy()
        for s, e, cost in edges:
            if memo[s] == -1e10: continue
            if tmp[e] < memo[s] - cost + income[e]:
                tmp[e] = memo[s] - cost + income[e]

        memo = tmp

    # 원래 negative cycle 체크
    # 위에서 negative cycle이 없는 경우의 최단 경로 구해진다
    # 만약 이때 적혀 있는 값보다 적은 값이 나오면 negative cycle 존재
    # for s, e, cost in edges:
    #     if memo[s] == 1e10: continue
    #     if memo[s] - cost + income[e] < memo[e]:
    #         return False
    # -> 지금 최대를 구하니 변형 필요

    # 2. 도시 도착 불가한 경우 -> 갱신이 아예 안 됐을 것
    if memo[end] == -1e10: return 'gg'

    # 3. positive cycle check
    for s, e, cost in edges:
        if memo[s] == -1e10: continue
        if memo[s] - cost + income[e] > memo[e]:
            # 가지고 있는 돈의 양이 더 커진다면
            # 최소 비용 간에는 음수 사이클로
            # 최소 비용이 더 줄어든다는 것
            # 그렇지만, 전체적인 돈 흐름은 비용이 감소하니 양수 사이클 -> +inf

            # 이 사이클이 end 지점에 영향을 주는 cycle이란 것을 체크 필요
            if check(e):  # e가 bfs로 end에 닿는지 체크
                return 'Gee'  # Gee 체크

    return memo[end]


N, start, end, M = map(int, input().split())
edges = []
adj = [[] for _ in range(N)]  # check 용
for _ in range(M):
    s, e, cost = map(int, input().split())
    edges.append((s, e, cost))
    adj[s].append(e)

income = list(map(int, input().split()))

print(bellmanFord())



'''
4 0 3 4
0 1 0
1 2 0
2 1 0
0 3 10
10 10 10 10
# 질문 게시판에서 발견한
# 사이클이 있지만 사이클이 도착지점에 영향을 주지 않는 경우
'''