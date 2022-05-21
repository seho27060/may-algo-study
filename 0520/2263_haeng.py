import sys
sys.setrecursionlimit(10**5)

def find(IN_s,IN_e,POST_e):
    if IN_e < IN_s:
        return
    head = postorder[POST_e]
    print(head, end=" ")
    I = inorder.index(head)
    find(IN_s,I-1,POST_e-(IN_e-I)-1)
    find(I+1,IN_e,POST_e-1)


n=int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
find(0,n-1,n-1)