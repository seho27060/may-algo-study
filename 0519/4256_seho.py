#220519 4256 트리
import sys
input = sys.stdin.readline

def post(preord, inord):

    if len(inord) == 1:
        print(inord[0], end=' ')
    else:
        for ridx in range(len(preord)):
            for idx in range(len(inord)):
                if preord[ridx] == inord[idx]:
                    post(preord[ridx+1:],inord[:idx])
                    post(preord[ridx+1:],inord[idx+1:])
                    print(inord[idx], end = ' ')
                    return
        return
tc_num = int(input())

for tc in range(tc_num):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))

    post(preorder, inorder)
    print()