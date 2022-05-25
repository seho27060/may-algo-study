
def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        ans.extend(preorder)
        return

    root = preorder[0]
    inidx = inorder.index(root)

    postorder(preorder[1:inidx + 1], inorder[:inidx])
    postorder(preorder[inidx + 1:], inorder[inidx + 1:])
    ans.append(root)


while True:
    try:
        lst = list(input().split())
        preorder = list(lst[0])
        inorder = list(lst[1])
    except:
        break

    ans = []
    postorder(preorder, inorder)
    for i in ans:
        print(i, end='')
    print()
