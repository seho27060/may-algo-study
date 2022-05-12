from collections import deque
import sys

def distance(a,b,c,d):
    return ((a-c)**2 + (b-d)**2)**0.5

def func(x1,y1,num):
    q = deque()
    q.append([x1,y1,num])
    while q:
        xx,yy,cnt = q.popleft()
        if xx == X and yy == Y:
            continue



        for j in range(1, len(lst)):
            XX,YY = lst[j]
            dis = distance(xx,yy,XX,YY)
            if dis == 50.0:
                cost = cnt +2
                if visited[j] > cost:
                    visited[j] = cost
                    q.append([XX,YY,cost])

            elif dis > 50:
                cost = (dis-50)/5 +2 +cnt
                if visited[j] > cost:
                    visited[j] = cost
                    q.append([XX,YY,cost])

            else:
                cost1 = (50-dis)/5 +2 + cnt
                cost2 = dis/5 + cnt
                cost = min(cost1,cost2)
                if visited[j] > cost:
                    visited[j] = cost
                    q.append([XX,YY,cost])


INF =sys.maxsize
x,y = map(float, input().split())
X,Y = map(float, input().split())
N = int(input())
lst = []
lst.append([x,y])
for _ in range(N):
    A,B = map(float, input().split())
    lst.append([A,B])
lst.append([X,Y])
visited = [INF]*(N+2)
visited[0] = 0

ho = []
for i in range(1, len(lst)):
    XX, YY = lst[i]
    cost = (distance(x, y, XX, YY) / 5)
    if visited[i] > cost:
        visited[i] = cost
        ho.append([XX,YY,cost])

for k in ho:
    x1,y1,num = k
    func(x1,y1,num)

print(visited[-1])