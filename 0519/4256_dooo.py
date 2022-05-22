def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        ans.append(preorder)
        return

    root = preorder[0]
    inidx = inorder.index(root)

    postorder(preorder[1:inidx + 1], inorder[:inidx])
    postorder(preorder[inidx + 1:], inorder[inidx + 1:])
    ans.append(root)


TC = int(input())
for _ in range(TC):
    ans = []
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(preorder, inorder)
    print(*ans)