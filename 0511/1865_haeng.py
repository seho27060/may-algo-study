def bf():
    result = [25000001] * (N + 1)

    for j in range(N):
        for now,next,cost in road:

            if result[next] > result[now] + cost:
                result[next] = result[now] + cost
                if j == N-1:
                    return True
    return False


TC = int(input())

for t in range(TC):
    N,M,W = map(int, input().split())
    road = []
    for _ in range(M):
        S,E,T = map(int, input().split())
        road.append((S,E,T))
        road.append((E,S,T))

    for _ in range(W):
        S,E,T = map(int,input().split())
        road.append((S,E,-T))


    if bf():
        print('YES')
    else:
        print('NO')
