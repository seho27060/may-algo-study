# 트리의 프리오더와 인오더를 이용한 포스트오더 출력문제
# 입력의 개수가 주어지지않으면 try-except를 사용하자

def find(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end='')
        return
    elif len(preorder) == 2:
        print(preorder[1], end='')
        print(preorder[0], end='')
        return

    idx = inorder.index(preorder[0])
    left_in = inorder[:idx]
    right_in = inorder[idx+1:]
    left_pre = preorder[1:len(left_in)+1]
    right_pre = preorder[len(left_pre)+1:]
    find(left_pre, left_in)
    find(right_pre, right_in)

    print(preorder[0], end='')

while True:
    try:
        n = input().split()
        n_1 = list(n[0])
        n_2 = list(n[1])
    except:
        exit()
    idx = n_2.index(n_1[0])
    find(n_1, n_2)
    print()