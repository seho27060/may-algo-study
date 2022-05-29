import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

#-------------------------------------------------------------------
def find(now,who,many):
    visited[now] = 1

    cnt=0
    for j in road[now]:
        if visited[j[0]]: continue
        cnt += find(j[0],j[1],j[2])


    if who == 'W':
        if cnt - many > 0:
            return cnt-many
        else:
            return  0
    elif who == 'S':
        return cnt+many

    return cnt
#-------------------------------------------------------------------


N = int(input())
road=[[] for _ in range(N+1)]
for i in range(2,N+1):
    t,a,p = input().split()
    a = int(a)
    p = int(p)
    road[i].append((p,t,a))
    road[p].append((i,t,a))
visited = [0] * (N+1)


print(find(1,0,0))