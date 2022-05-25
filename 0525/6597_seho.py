#220525 6597 트리 복구
# 프리오더, 인오더 주어졌을때, 포스트오더 출력하기.
# 총 26자.
import sys
input = sys.stdin.readline

def postorder(preord, inord):

    if len(inord) == 1:
        print(inord[0], end="")
    else:
        for ridx in range(len(preord)):
            for idx in range(len(inord)):
                if preord[ridx] == inord[idx]:
                    postorder(preord[ridx+1:], inord[:idx])
                    postorder(preord[ridx+1:],inord[idx+1:])
                    print(inord[idx], end = '')
                    return
        return
while 1:
    getput = "" + input()
    try:
        preorder, inorder = getput.split()
        postorder(preorder, inorder)
        print()
    except:
        break


