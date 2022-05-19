def postorder(root, start, end):
    if start < end:
        idx = inorder.index(preorder[root])
        postorder(root+1, start, idx)
        postorder(root+1+idx-start, idx+1, end)
        print(preorder[root], end=" ")

tc = int(input())
for _ in range(tc):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(0, 0, n)
    print()