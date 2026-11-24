import heapq

INF = 9999999

def dijkstra(graph, start):
    V = len(graph)
    pred = [-1] * V
    dist = [INF] * V
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return pred, dist

def get_path(pred, target):
    path = []
    curr = target
    while curr != -1:
        path.append(str(curr + 1))
        curr = pred[curr]
    return " -> ".join(reversed(path))

# списки суміжності графа 
G = [
    [(1, 6), (2, 2), (3, 4)],                 # 1
    [(0, 6), (3, 6), (5, 6)],                 # 2
    [(0, 2), (7, 4)],                         # 3
    [(0, 4), (1, 6), (4, 1)],                 # 4
    [(3, 1), (5, 4), (6, 7)],                 # 5
    [(1, 6), (4, 4), (6, 5), (7, 3)],         # 6
    [(4, 7), (5, 5), (7, 5)],                 # 7
    [(2, 4), (5, 3), (6, 5)]                  # 8
]

start_node = 0  # вершина 1
pred, dist = dijkstra(G, start_node)

print(f"Найкоротші шляхи від вершини {start_node + 1}:")
print(f"{'З':<3} {'В':<3} {'Шлях':<20} {'Вага'}")
for i in range(len(G)):
    if i != start_node:
        print(f"{start_node + 1:<3} {i + 1:<3} {get_path(pred, i):<20} {dist[i]}")