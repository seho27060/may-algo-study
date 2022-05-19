T=int(input())
for t in range(T):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))

    postorder = []

    def find(PRE,IN):
        if len(PRE) == 0:
            return
        if len(PRE) == 1:
            postorder.append(PRE[0])
            return

        for i in range(n):
            if IN[i] == PRE[0]:
                I = i
                break
        left_in = IN[0:I]
        right_in = IN[I+1:n]


        left_pre = PRE[1:len(left_in)+1]
        right_pre = PRE[len(left_in)+1:]

        find(left_pre,left_in)
        find(right_pre,right_in)
        postorder.append(IN[I])


    find(preorder,inorder)

    print(*postorder)