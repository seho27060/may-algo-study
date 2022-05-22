import sys
sys.setrecursionlimit(100000)
# 인덱스를 활용한 프리오더 찾기

def find(i_s, i_e, p_s, p_e):
    print(postorder[p_e], end=' ')
    if p_e == p_s:
        return
    if p_e - p_s == 1:
        print(postorder[p_s], end=' ')
        return

    root = inorder.index(postorder[p_e])
    if i_s <= root-1:
        find(i_s, root-1, p_s, p_s + root - i_s - 1)
    if root+1 <= i_e:
        find(root+1, i_e, p_s + root - i_s, p_e-1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
find(0, n-1, 0, n-1)
print()