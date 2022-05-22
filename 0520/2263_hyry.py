import sys
sys.setrecursionlimit(10**5)


# def preOrder(A, B):
#     # print(A, B)
#     if A and B:
#         root = B[-1]
#         mid = A.index(root)
#         print(root, end=" ")
#         # preOrder(A[:mid], B[:mid])
#         # preOrder(A[mid+1:], B[mid:-1])


def preOrder(startA, endA, startB, endB):

    if startA <= endA and startB <= endB:

        root = B[endB]
        print(root, end=" ")
        mid = A.index(root)

        preOrder(startA, mid - 1, startB, startB + mid - startA - 1)  
        preOrder(mid + 1, endA, startB + mid - startA, endB - 1)


N = int(input())
A = list(map(int, input().split()))  # in
B = list(map(int, input().split()))  # post

preOrder(0, N - 1, 0, N - 1)

