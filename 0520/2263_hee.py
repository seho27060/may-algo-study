import sys
sys.setrecursionlimit(10**5)

def tree(S, E, I):
    idx = inorder.index(postorder[I])
    ans.append(postorder[I])
    if S < idx:
        tree(S, idx - 1, I + idx - E - 1)

    if idx < E:
        tree(idx + 1, E, I - 1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
ans = []
tree(0, n - 1, n - 1)
print(*ans)