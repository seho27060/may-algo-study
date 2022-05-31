#220531 14725 개미굴
# 입력값을 토대로 트리를 만들자!
# 루트노드 다음 노드 - 주루룱 순서로 입력됨
# 출력은 사전순으로 할것. -> ?
# n < 1000,

import sys
input = sys.stdin.readline

n = int(input())

getList = []
for _ in range(n):
    txtGet = input().split()
    txtLen = int(txtGet[0])
    txtList = txtGet[1:].copy()
    getList.append(txtList)
getList.sort()

answer = []


for idx in range(n):
    listGet = getList[idx]
    if answer:
        getIdx = 0
        prevGet = getList[idx-1]
        for countIdx in range(len(listGet)):
            if prevGet[countIdx] != listGet[countIdx] or len(prevGet) <= countIdx:
                break
            else:
                getIdx = countIdx + 1
        for c in range(getIdx, len(listGet)):
            result = "--"*c + listGet[c]
            answer.append(result)
    else:
        for getIdx in range(len(listGet)):
            result = "--" * getIdx + listGet[getIdx]
            answer.append(result)

for i in range(len(answer)):
    print(answer[i])

