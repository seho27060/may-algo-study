def check(x2):
    visited = [False]*N
    ST=[x2]
    while ST:
        node = ST.pop(0)
        if node == E:
            return True
        visited[node] = True

        for k in road:
            if k[0] == node and visited[k[1]] == False:
                ST.append(k[1])
    return False


def bf(x):
    result[x] = money[x]
    for i in range(N):
        for j in road:
            now = j[0]
            next = j[1]
            cost = j[2]
            gain = money[j[1]]

            if result[now] != -50000001 and result[next] < result[now]-cost+gain:
                result[next]=result[now]-cost+gain
                if i == N-1:
                    # 갱신된 노드가 경로에 해당될경우만 True로 리턴되게 만들어야함
                    if check(next):
                        return True
    return False


N,S,E,M = map(int,input().split())
road=[]

for _ in range(M):
    road.append(list(map(int,input().split())))
money=list(map(int, input().split()))

result=[-50000001]*N


if bf(S):
    if result[E] == -50000001:
        print('gg')
    else:
        print('Gee')
else:
    if result[E] == -50000001:
        print('gg')
    else:
        print(result[E])


