n = int(input())
graph = {}
for _ in range(n):
    line = input().split()
    nodes = line[1:]
    cur = graph
    for node in nodes:
        if node not in cur:
            cur[node] = {}
        cur = cur[node]

def search(level, graph):
    graph = dict(sorted(graph.items()))
    for child in graph:
        print("--"*level + child)
        search(level+1, graph[child])

search(0, graph)