# 벨만포드 기본원리 문제
# 노드 수만큼 반복 후 한번 더 진행하여 음의 순환을 확인
# 그 후에 출력 규칙에 맞게 조건 설정

def bf():
    D = [1000000000000] * (N+1)
    D[1] = 0
    for i in range(N):
        for j in range(1, N+1):
            if D[j] != 1000000000000:
                for B, C in Bus[j]:
                    if D[B] > D[j] + C:
                        D[B] = D[j] + C

    for i in range(1, N+1):
        if D[i] != 1000000000000:
                for B, C in Bus[i]:
                    if D[B] > D[i] + C:
                        print(-1)
                        return

    for i in range(2, N+1):
        if D[i] == 1000000000000:
            print(-1)
        else:
            print(D[i])


N, M = map(int, input().split())
Bus = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    Bus[A].append((B, C))
bf()