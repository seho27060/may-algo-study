import heapq
import sys
input = sys.stdin.readline
# 경로저장을 위해 깊은복사를 써버렸습니다...다음에는 다른 방법을 찾아보자...
# 최단거리를 찾을때마다 경로에 추가시켜가며 저장 후 목적지일때는 판단을 통해 건우를 데려갈지 결정
def dijk():
    ans_dis = -1
    D = [1000000000] * (V+1)
    D[1] = 0
    q = []
    heapq.heappush(q, (D[1], 1, [1]))
    while q:
        dis, now, root = heapq.heappop(q)
        if dis > D[V]:
            continue
        for e, d in G[now]:
            if D[e] >= dis + d:
                D[e] = dis + d
                root.append(e)
                heapq.heappush(q, (D[e], e, root[::]))
                if e == V:
                    if ans_dis == -1 or ans_dis > D[V]:
                        ans_dis = D[V]
                        if P in root:
                            flag = True
                        else:
                            flag = False
                    elif ans_dis == D[V]:
                        if not flag and P in root:
                            flag = True
                root.pop()
    if flag:
        return print('SAVE HIM')
    else:
        return print('GOOD BYE')




V, E, P = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    G[s].append((e, d))
    G[e].append((s, d))
dijk()