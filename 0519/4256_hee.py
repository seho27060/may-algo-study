def postorder(root):
    left, right = G[root]
    if left != 0:
        postorder(left)
    if right != 0:
        postorder(right)
    ans.append(root)

def tree(S, E, P, I):
    idx = inorder.index(preorder[I])

    if G[P][0] == 0:
        G[P][0] = preorder[I]
    else:
        G[P][1] = preorder[I]

    if idx > S:
        tree(S, idx-1, preorder[I], I + 1)
    if idx < E:
        tree(idx+1, E, preorder[I], I + idx - S + 1)

for _ in range(int(input())):
    n = int(input())
    G = [[0, 0] for _ in range(n + 1)]
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    tree(0, n-1, 0, 0)

    ans = []
    postorder(preorder[0])
    print(*ans)