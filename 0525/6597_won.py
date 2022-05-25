import sys
input = sys.stdin.readline

def postOrder(preOrder, inOrder):
    global ans
    if len(preOrder) == 0:
        return
    if len(preOrder) == 1:
        ans += preOrder[0]
        return
    i = inOrder.index(preOrder[0])
    leftIn = inOrder[:i]
    rightIn = inOrder[i + 1:n]

    leftPre = preOrder[1:len(leftIn) + 1]
    rightPre = preOrder[len(leftIn) + 1:]

    postOrder(leftPre, leftIn)
    postOrder(rightPre, rightIn)
    ans += inOrder[i]

while True:
    try:
        preOrder, inOrder = input().split()
        n = len(preOrder)
        ans = ''
        postOrder(preOrder, inOrder)
        print(ans)
    except:
        exit()
