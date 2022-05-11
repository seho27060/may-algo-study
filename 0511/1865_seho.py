### 220511. 1865 웜홀
# 도로 = 양방향, +, 중복가능
# 웜홀 = 단방향, -,

# 모든 지점에서 출발했을때, 시간 역행이 가능한가?
# 모든 지점을 통틀어서 음수의 사이클이 존재한다면...
# 최단거리 or 최장거리로 이동하는게 아니기때문에
# 사이클이 있는지, 없는지만 판단하면 된다.
import sys
input = sys.stdin.readline
INF = sys.maxsize

def BF(start):
    global loads, n, m
    dst = [INF]*(n+1)
    dst[start] = 0

    for i in range(n-1):
        for now in range(n+1):
                for nxt, cost in loads[now]:
                    if dst[nxt] > dst[now] + cost:
                        dst[nxt] = dst[now] + cost

    for now in range(n+1):
        for nxt, cost in loads[now]:
            if dst[nxt] > cost + dst[now]:
                return True
    return False

tc_num = int(input())

for tc in range(tc_num):
    n, m, w = map(int,input().split())
    loads = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int,input().split())
        loads[s].append([e,t])
        loads[e].append([s,t])

    for _ in range(w):
        s, e, t = map(int,input().split())

        loads[s].append([e,-t])

    answer = BF(0)
    if answer:
        print("YES")
    else:
        print("NO")