import sys
input = sys.stdin.readline

def tree(S, E, I):
    idx = inorder.index(preorder[I])
    if S < idx:
        tree(S, idx-1, I + 1)
    if idx < E:
        tree(idx+1, E, I - S + idx + 1)
    ans.append(preorder[I])

while True:
    try:
        preorder, inorder = map(str, input().split())
    except:
        break

    ans = []
    tree(0, len(preorder)-1, 0)
    print(''.join(ans))