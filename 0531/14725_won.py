import sys
input = sys.stdin.readline


N = int(input())
ant = []
for _ in range(N):
    arr = input().split()
    K = int(arr[0])
    ant.append(arr[1:])
ant.sort()

for i in range(N):
    if i == 0:
        for k in range(len(ant[i])):
            print('--' * k + ant[i][k])
    else:
        cnt = -1
        for k in range(len(ant[i])):
            if len(ant[i - 1]) - 1 < k or ant[i][k] != ant[i - 1][k]:
                break
            else:
                cnt = k
        for k in range(cnt + 1, len(ant[i])):
            print('--' * k + ant[i][k])

