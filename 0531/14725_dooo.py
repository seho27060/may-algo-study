
n = int(input())
arr = []
for _ in range(n):
    lst = list(input().split())
    arr.append(lst[1:])
arr.sort()

for i in range(len(arr[0])):
    print("--" * i + arr[0][i])
for i in range(1, n):
    cnt = -1
    for j in range(len(arr[i])):
        if len(arr[i - 1]) <= j or arr[i - 1][j] != arr[i][j]:
            break
        else:
            cnt = j
    for j in range(cnt + 1, len(arr[i])):
        print("--" * j + arr[i][j])