class Graph:
    def __init__(self, graph):
        self.graph = graph

    def ucs(self, start, goal):
        visited = set()
        queue = [(0, start, [start])]
        while queue:
            cost, node, path = queue.pop(0)
            if node == goal:
                return path, cost
            if node not in visited:
                visited.add(node)
                for neighbor, weight in self.graph[node].items():
                    if neighbor not in visited:
                        new_cost = cost + weight
                        new_path = path + [neighbor]
                        queue.append((new_cost, neighbor, new_path))
                queue.sort()
        return "No Path Found..", float('inf')

if __name__ == "__main__":
    graph = {}
    num_edges = int(input("Enter the number of Edges: "))
    print("|| FORMAT: node neighbor weight ||")
    for _ in range(num_edges):
        while True:
            try:
                u, v, weight = input("Enter Edge: ").split()
                weight = int(weight)
                if u not in graph:
                    graph[u] = {}
                graph[u][v] = weight
                break
            except ValueError:
                print("Invalid input format. Please use: node neighbor weight")
    
    g = Graph(graph)
    start_node = input("Enter start node: ")
    goal_node = input("Enter goal node: ")
    best_path, min_cost = g.ucs(start_node, goal_node)

    if best_path == "No Path Found..":
        print(best_path)
    else:
        print("Best Path:", best_path)
        print("Minimum Cost:", min_cost)