import sys
input = sys.stdin.readline

def f():
    money[1] = 0
    for i in range(n):
        for curN in range(1, n + 1):
            for newN, newM in G[curN]:
                if money[curN] == INF:
                    continue

                if money[newN] < money[curN] + newM:
                    money[newN] = money[curN] + newM
                    path[newN] = curN

                    if i == n - 1:
                        money[newN] = -INF

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
INF = -100000001
money = [INF] * (n + 1)
path = [0] * (n + 1)
result = f()
ans = []



if money[n] == -INF:
    print(-1)
else:
    ans.append(n)

    while True:
        n = path[n]
        ans.append(n)
        if n == 1:
            break
    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end=" ")
    print()
