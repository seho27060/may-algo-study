import sys
input = sys.stdin.readline


def postOrder(preOrder, inOrder):
    global ans
    if len(preOrder) == 0:
        return
    if len(preOrder) == 1:
        ans += preOrder
        return

    root = preOrder[0]
    inOrderIdx = inOrder.index(root)

    postOrder(preOrder[1:inOrderIdx + 1], inOrder[:inOrderIdx])
    postOrder(preOrder[inOrderIdx + 1:], inOrder[inOrderIdx + 1:])
    ans.append(root)

T = int(input())
for _ in range(T):
    n = int(input())
    ans = []
    preOrder = list(map(int, input().split()))
    inOrder = list(map(int, input().split()))
    postOrder(preOrder, inOrder)
    print(*ans)


