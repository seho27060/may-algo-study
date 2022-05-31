import sys
input = sys.stdin.readline
N = int(input())
G = dict()

def structure(num, S):
    temp = sorted(list(S.keys()))
    for s in temp:
        print('--' * num + s)
        structure(num+1, S[s])

for _ in range(N):
    A = list(map(str, input().split()))
    K, D = int(A[0]), A[1:]
    P = G
    for i in D:
        if i not in P.keys():
            P[i] = dict()
        P = P[i]

structure(0, G)