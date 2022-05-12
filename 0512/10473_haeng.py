import heapq
import sys
input = sys.stdin.readline

def pythagoras(x,y):
    return (x**2 + y**2) **(1/2)


X,Y=map(float,input().split())
targetX,targetY=map(float,input().split())

N=int(input())
cannon = []

for _ in range(N):
    cannon.append(list(map(float, input().split())))
cannon.append([targetX,targetY])
direct = pythagoras(targetX-X,targetY-Y)/5
result = [direct]*(N+1)
ST = []


for i in range(N):
    p = pythagoras(cannon[i][0]-X,cannon[i][1]-Y)
    if result[i] > p/5:
        result[i] = p/5
        heapq.heappush(ST, (p/5, i))


while ST:
    cnt,now = heapq.heappop(ST)

    for j in range(N+1):
        if j == now: continue
        cP = pythagoras(cannon[now][0]-cannon[j][0],cannon[now][1]-cannon[j][1])
        ride = abs((cP-50)/5) + 2 + cnt
        walk = cP / 5 + cnt

        short = min(ride,walk)

        if result[j] > short:
            result[j] = short
            if j != N:
                heapq.heappush(ST, (short,j))

print(result[N])

