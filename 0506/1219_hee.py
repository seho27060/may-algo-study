from collections import defaultdict, deque
import sys
INF = sys.maxsize
input = sys.stdin.readline

def bfs(S, E):
    V = [False] * N
    Q = deque([S])
    while Q:
        n1 = Q.popleft()

        if n1 == E:
            return True

        for t, n2 in G[n1]:
            if not V[n2]:
                Q.append(n2)
                V[n2] = True
    return False

N, S, E, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    s, e, c = map(int, input().split())
    G[s].append((c, e))
A = list(map(int, input().split()))

# 기본적으로 벨만포드 알고리즘은 N-1번 돌았을 때 수렴하게 되어있음
# 하지만 싸이클을 갖는 경우에는 그 이후에도 테이블이 업데이트 되는 현상이 발생
# 즉 N번 째에서도 테이블이 업데이트 된다는 것은 싸이클을 갖는다는 것

D = [-INF] * N
D[S] = A[S]
for i in range(N):
    for j in range(N):
        if D[j] == -INF:
            continue
        # 기본적으로 현재 노드가 -INF인 경우에는 갱신을 진행하지 않기 때문에 continue
        for trans, n2 in G[j]:
            if A[n2] - trans + D[j] > D[n2]:
                D[n2] = A[n2] - trans + D[j]
                # Dijkstar 테이블 업데이트
                if i == N-1:
                    # 만약 N-1에도 테이블이 업데이트 된다면 무한하게 증가할 가능성이 있음
                    #BFS로 목적지에 갈 수 있는 노드가 갱신되는 것인지 체크
                    # 다른 코드 구경해보면 bfs(n2, E)로만 체크하던데... bfs(S,j)는 어떻게 보장이 되는지... 좀더 생각해봐야함
                    # 이라고 쓰는 순간 보장이 안 됐으면 D[j]가 -INF 였을 듯 ㅠ
                    if bfs(n2, E):
                        print('Gee')
                        exit(0)
if D[E] == -INF:
    print('gg')
else:
    print(D[E])


