import sys
sys.setrecursionlimit(10**9)

def preorder(instart, poststart, end):
    if poststart <= end:
        print(postorder[end], end=" ")
        root = indic[postorder[end]]
        leftnum = root-instart
        preorder(instart, poststart, poststart+leftnum-1)
        preorder(root+1, poststart+leftnum, end-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
indic = {}
for i in range(n):
    indic[inorder[i]] = i
preorder(0, 0, n-1)