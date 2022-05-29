import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# dfs를 활용 늑대와 양의 배열을 따로 만들어 문제를 푼다.
def dfs(num):
    val = s[num]
    for i in arr[num]:
        val += dfs(i)
    if w[num] != 0:
        if  val < w[num]:
            w[num] -= val
            val = 0
        else:
            val -= w[num]
            w[num] = 0
    return val

N = int(input())
w = [0] * (N+1)
s = [0] * (N+1)
arr = [[] for _ in range(N+1)]
for i in range(2, N+1):
    t, a, p = input().split()
    a = int(a)
    p = int(p)
    if t == 'W':
        w[i] = a
    else:
        s[i] = a
    arr[p].append(i)
print(dfs(1))