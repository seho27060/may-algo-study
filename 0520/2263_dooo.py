import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = [0] + list(map(int, input().split()))
postorder = [0] + list(map(int, input().split()))
ans = []

lst = [0] * (n + 1)
for i in range(n + 1):
    lst[inorder[i]] = i


def preorder(ins, ine, posts, poste):
    if (ins > ine) or (posts > poste):
        return
    root = postorder[poste]
    sec = lst[root] - ins
    ans.append(root)

    preorder(ins, lst[root] - 1, posts, posts+sec-1)
    preorder(lst[root] + 1, ine, posts+sec, poste - 1)


preorder(1, n, 1, n)
print(*ans)