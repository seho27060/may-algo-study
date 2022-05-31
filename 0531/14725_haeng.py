import sys
input = sys.stdin.readline


N = int(input())
itemlist = []
for _ in range(N):
    itemlist.append(list(input().split()[1:]))
itemlist.sort()

root=[]
root2={}
while itemlist:
    item = itemlist.pop(0)
    head = item.pop(0)

    if head not in root:
        print(head)
        root.append(head)
        root2[head]=[]

    for i in range(len(item)):
        if item[0:i+1] in root2[head]:
            continue
        print('--'*(i+1) + item[i])
        root2[head].append(item[0:i+1])
