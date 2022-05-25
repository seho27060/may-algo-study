def postorder(root, start, end):
    if start < end:
        idx = inorder.index(preorder[root])
        postorder(root+1, start, idx)
        postorder(root+1+idx-start, idx+1, end)
        print(preorder[root], end="")

while True:
    try:
        preorder, inorder = map(list, input().split())
        postorder(0, 0, len(preorder))
        print()
    except EOFError:
        break