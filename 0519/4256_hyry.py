
import sys
input = sys.stdin.readline


def postOrder(A, B):
    if A and B:
        root = A[0]
        mid = B.index(root)

        postOrder(A[1: mid + 1], B[:mid])
        postOrder(A[mid + 1:], B[mid + 1:])

        nodes.append(root)


T = int(input())
for _ in range(T):
    n = int(input())
    preO = list(map(int, input().split()))
    inO = list(map(int, input().split()))

    nodes = []
    postOrder(preO, inO)

    print(*nodes)

