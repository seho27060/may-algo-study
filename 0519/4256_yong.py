# pre, in 정렬 방식을 기반으로 root를 찾아 좌우 노드를 분리하는 방법
# preorder의 첫 값이 root이니 길이를 기준으로 출력 결정
def find(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], end=' ')
        print(preorder[0], end=' ')
        return

    idx = inorder.index(preorder[0])
    left_in = inorder[:idx]
    right_in = inorder[idx+1:]
    left_pre = preorder[1:len(left_in)+1]
    right_pre = preorder[len(left_pre)+1:]
    find(left_pre, left_in)
    find(right_pre, right_in)

    print(preorder[0], end=' ')


T = int(input())

for _ in range(1, T+1):
    n = int(input())
    n_1 = list(map(int, input().split()))
    n_2 = list(map(int, input().split()))
    idx = n_2.index(n_1[0])
    find(n_1, n_2)
    print()