def tsp_bfs(graph, start):
    visited = set([start])
    queue = [(start, [start], 0)]

    while queue:
        current_city, path, cost = queue.pop(0)

        if len(path) == len(graph):
            path.append(start)
            cost += graph[current_city][start]
            return path, cost

        for neighbor in graph[current_city]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                new_cost = cost + graph[current_city][neighbor]
                queue.append((neighbor, new_path, new_cost))

    return None


graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 3},
    'D': {'A': 1, 'B': 2, 'C': 3}
}

start_city = 'A'
result = tsp_bfs(graph, start_city)

if result:
    path, cost = result
    print(f'TSP Path: {path}')
    print(f'Total Cost: {cost}')
else:
    print('No Hamiltonian cycle found.')
