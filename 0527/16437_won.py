import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
node = [[] for _ in range(N + 1)]
node[1] = ['SS', 0, 0]
child = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    t, a, p = input().split()
    a = int(a)
    p = int(p)
    node[i] = [t, a, p]
    child[p].append(i)

def f(cur):
    sum = 0
    for new in child[cur]:
        sum += f(new)
    if node[cur][0] == 'S':
        sum += node[cur][1]
    else:
        sum -= node[cur][1]

    if sum < 0:
        sum = 0
    return sum

ans = f(1)
print(ans)
