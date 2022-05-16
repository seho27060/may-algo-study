def bf():
    for i in range(N):
        for now,next,time in Mlist:
            if result[now] != 5000001 and result[next] > result[now]+time:
                result[next]=result[now]+time
                if i == N-1:
                    return True
    return False


N,M = map(int,input().split())
Mlist=[]
for i in range(M):
    Mlist.append(list(map(int,input().split())))

result=[5000001]*(N+1)
result[1] = 0

if bf():
    print(-1)
else:
    for j in range(2,N+1):
        if result[j] == 5000001:
            print(-1)
        else:
            print(result[j])