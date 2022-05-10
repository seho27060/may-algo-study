def belman_ford(S, E):
    INF = float('inf')
    earn_list = [INF] * N
    earn_list[S] = -benefit[S]
    for _ in range(M):
        for node in range(N):
            for next_node in bus_pay[node]:
                next_pay = bus_pay[node][next_node]
                if earn_list[next_node] > earn_list[node] + next_pay - benefit[next_node]:
                    earn_list[next_node] = earn_list[node] + next_pay - benefit[next_node]

    cycle_node = set()
    for _ in range(M):
        for node in range(N):
            for next_node in bus_pay[node]:
                next_pay = bus_pay[node][next_node]
                if earn_list[next_node] > earn_list[node] + next_pay - benefit[next_node]:
                    earn_list[next_node] = earn_list[node] + next_pay - benefit[next_node]
                    cycle_node.add(next_node)
                    cycle_node.add(node)
    if earn_list[E] == INF:
        print('gg')
    else:
        if len(cycle_node) > 0:
            visted = [False] * N
            path_list = list(cycle_node)
            while path_list:
                node = path_list.pop(0)
                for next_node in bus_pay[node]:
                    if visted[next_node] == False:
                        visted[next_node] = True
                        path_list.append(next_node)
            if visted[E]:
                print('Gee')
                return
            else:
                print(-earn_list[E])
        else:
            print(-earn_list[E])


N, start_city, end_city, M = map(int, input().split())

bus_pay = [{} for _ in range(N)]
for _ in range(M):
    a_city, b_city, pay = map(int, input().split())
    bus_pay[a_city][b_city] = min(bus_pay[a_city].get(b_city, float('inf')), pay)

benefit = list(map(int, input().split()))

belman_ford(start_city, end_city)