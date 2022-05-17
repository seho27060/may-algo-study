import sys
input = sys.stdin.readline
# 경로찾기 문제
# 메모리 절약을 위해 정답은 재귀로 하나씩 출력
# 경로 저장용 visited와 싸이클 확인용 check를 만들어 이를 활용해 정답찾기

def bf():
    D = [-1000000000000] * (n + 1)
    D[1] = 0
    visited[1] = 0
    for i in range(n):
        for j in range(1, n + 1):
            if D[j] != -1000000000000:
                for v, w in R[j]:
                    if D[v] < D[j] + w:
                        D[v] = D[j] + w
                        visited[v] = j
    if D[-1] == -1000000000000:
        return False
    for j in range(1, n + 1):
        if D[j] != -1000000000000:
            for v, w in R[j]:
                if D[v] < D[j] + w:
                    D[v] = D[j] + w
                    check[j] = 1
                    check[v] = 1
    for j in range(1, n + 1):
        if D[j] != -1000000000000 and check[j] == 1:
            for v, w in R[j]:
                check[v] = 1
    if check[n]:
        return False
    return True

def ansPrint(n):
    if n != 1:
        ansPrint(visited[n])
    print(n, end=' ')


n, m = map(int, input().split())
R = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
check = [0] * (n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    R[u].append((v, w))
if bf():
    ansPrint(n)
else:
    print(-1)