# 첫 배열인경우와 아닌경우로 나눠서 풀이
# 첫 배열이 아니라면 이전배열과 같은지 아닌지에 따라 판단
N = int(input())
G = []

for i in range(N):
    arr = list(input().split())
    G.append(arr[1:])

G.sort()
for i in range(N):
    if i == 0:
        for j in range(len(G[i])):
            print('--'*j + G[i][j])
    else:
        cnt = -1
        for j in range(len(G[i])):
            if len(G[i-1]) <= j or G[i-1][j] != G[i][j]:
                break
            else:
                cnt = j
        for j in range(cnt+1, len(G[i])):
            print('--'*j + G[i][j])