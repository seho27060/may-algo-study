
from collections import defaultdict

def bellmanFord():
    MAP = [[1e10] * C for _ in range(R)]
    MAP[0][0] = 0

    # for _ in range((R - 1) + (C - 1)):  # 틀린 지점!
    # 만들기는 노드로 만들어 놓고 그래프로 계산한
    # 한계점으로 둬서 틀림
    # 최대 = 노드 개수 만큼
    for _ in range(R * C):
        tmp = MAP.copy()
        for (curR, curC) in edges.keys():
            if MAP[curR][curC] == 1e10: continue
            for cost, neiR, neiC in edges[(curR, curC)]:
                if tmp[neiR][neiC] > MAP[curR][curC] + cost:
                    tmp[neiR][neiC] = MAP[curR][curC] + cost
        MAP = tmp

    # 글이 너무 불친절해서 헷갈릴 수 있는데
    # 상근이는 항상 무조건 빨리 가는 것이 목적이니
    # 목적지에 닿는지 여부와 상관 없이 빠른 루트를 타게 되어 있다
    # impossible과 never이 공존할 수 있는 상황에선 무조건 Never가 먼저
    for (curR, curC) in edges.keys():
        if MAP[curR][curC] == 1e10: continue
        for cost, neiR, neiC in edges[(curR, curC)]:
            if MAP[neiR][neiC] > MAP[curR][curC] + cost:
                return "Never"

    if MAP[R - 1][C - 1] == 1e10: return "Impossible"

    return MAP[R - 1][C - 1]


while True:
    C, R = map(int, input().split())
    if R == C == 0: break

    G = int(input())
    graves = set()
    for _ in range(G):
        c, r = map(int, input().split())
        graves.add((r, c))

    E = int(input())
    holes = dict()
    edges = defaultdict(list)
    for _ in range(E):
        c1, r1, c2, r2, t = map(int, input().split())
        holes[(r1, c1)] = (r2, c2, t)
        edges[(r1, c1)].append((t, r2, c2))


    # 이차원 배열 풀려고 봤더니 힘들 것 같아
    # 벨만포드는 역시 노드로 봐야한다고 생각하고
    # 배열 -> 노드로 변환
    for row in range(R):
        for col in range(C):
            # 볼 때마다 바로 이해하려고 그냥 continue를 분리해서 작성
            if (row, col) == (R - 1, C - 1): continue # 도착 지점
            if (row, col) in graves: continue # 묘석
            if (row, col) in holes: continue # 구멍
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                newR, newC = row + dr, col + dc
                if 0 <= newR < R and 0 <= newC < C and (newR, newC) not in graves:
                    edges[(row, col)].append((1, newR, newC))


    print(bellmanFord())


'''
3 3
0
2
1 2 0 2 -1
2 1 2 2 3
0 0
# 6 

3 3
0
2
1 2 0 2 -3
2 1 2 2 3
0 0
#Never 

3 3
0
2
1 2 0 2 2
2 1 2 2 3
0 0
# 6

3 3
0
3
2 0 0 0 -1
1 1 0 0 -1
0 2 0 0 -1
0 0
# Impossible

3 3
0
1
1 1 2 2 -5
0 0
# -3

3 3
0
1
0 0 1 1 -4
0 0
# Never (올바른 테케는 아님)

5 5
0
1
2 2 1 1 -5
0 0
# Never

'''