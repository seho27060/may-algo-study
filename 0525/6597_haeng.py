preorder,inorder= list(map(str, input().split()))
n=len(preorder)
postorder = ''


def find(PRE, IN):
    global postorder
    if len(PRE) == 0:
        return
    if len(PRE) == 1:
        postorder += PRE[0]
        return
    I = IN.index(PRE[0])
    left_in = IN[0:I]
    right_in = IN[I + 1:n]
    left_pre = PRE[1:len(left_in) + 1]
    right_pre = PRE[len(left_in) + 1:]

    find(left_pre, left_in)
    find(right_pre, right_in)
    postorder += IN[I]

find(preorder, inorder)

print(postorder)