#220522 2263 트리의 순회

# 중위순회와 후위순회가 주어졌을때, 전위순회 구하라
# n <= 100,000
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def preorder(inStart, inEnd, postStart, postEnd):
    global postorder, position
    if inStart > inEnd or postStart > postEnd:
        return
    result = postorder[postEnd]
    print(result, end= ' ')

    left = position[result] - inStart
    right = inEnd - position[result]

    preorder(inStart, inStart+left-1, postStart, postStart+left-1)
    preorder(inEnd-right+1, inEnd,postEnd-right, postEnd-1)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
# preorder(inord 시작, inord 끝, post시작, post끝)
position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i

preorder(0, n-1,0,  n-1)