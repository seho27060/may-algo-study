import sys
input = sys.stdin.readline

def postOrder(A, B):
    if A and B:
        root = A[0]
        mid = B.index(root)

        postOrder(A[1:], B[:mid])
        postOrder(A[mid + 1:], B[mid + 1:])

        print(root, end="")


while True:
    try:
        A, B = input().split()  # A = pre, B = in
        postOrder(A, B)
        print()
    except:
        break