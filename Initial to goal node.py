 import heapq
def ucs(graph, start, end):
    heap = [(0, start)]
    visited = set([start])
    while heap:
        cost, node = heapq.heappop(heap)
        if node == end:
            return cost
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost + graph[node][neighbor], neighbor))
                visited.add(neighbor)
    return float('inf')

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 1, 'E': 3},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 2},
    'F': {},
}
print(ucs(graph,'A','F'))
