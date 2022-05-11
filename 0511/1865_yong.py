import sys
input = sys.stdin.readline
# 벨만포드 문제, 음수사이클 존재 유무로 가능성 여부를 판단
# 진행 단계를 줄이기 위해 방문 안해본 노드도 다 방문시켜서 한번에 처리
# 이게...맞는건가???
TC = int(input())

def bm():
    D = [1000000000] * (N+1)
    D[1] = 0
    for i in range(N-1):
        for j in range(1, N+1):
            for e, t in Root[j]:
                if D[e] > D[j] + t:
                    D[e] = D[j] + t
    for i in range(1, N+1):
        for e, t in Root[i]:
            if D[e] > D[i] + t:
                return print('YES')
    return print('NO')

for i in range(TC):
    N, M, W = map(int, input().split())
    Root = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, t = map(int, input().split())
        Root[s].append((e, t))
        Root[e].append((s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        Root[s].append((e, -t))
    bm()