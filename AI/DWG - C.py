#Directed Weighted Graph w/ Cost
# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_edge(self,u,v,weight):
#         if u not in self.graph:
#             self.graph[u] = []
#         self.graph[u].append((v,weight))

#     def display(self):
#         result = " "
#         for node in self.graph:
#             for neighbor , weight in self.graph[node]:
#                     result += f"({node} --> {neighbor} , Weight : {weight})\n"
#         return result.strip()
    
# if __name__ == "__main__":
#     g = Graph()
#     print("MENU\nEnter an edge [Format Node Vertice Weight]\nor\nType done to finish" )
#     while True:
#         edge_input = input("Enter Input: ")
#         if edge_input.lower() == "done":
#             break
#         u,v,weight = map(int , edge_input.split())
#         g.add_edge(u,v,weight)
    
#     print("The graph is ---->")
#     print("\n"+g.display()+"\n")

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def display(self):
        result = ""  # Modified to build a string
        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                result += f"({node} --> {neighbor} , Weight : {weight})\n"
        return result.strip()

    def calculate_cost(self, start, end):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()
        current = start

        while current:
            visited.add(current)
            neighbors = self.graph[current]

            for neighbor, weight in neighbors:
                if neighbor not in visited:
                    new_distance = distances[current] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

            # Find next unvisited node with the minimum distance
            next_node = None
            min_distance = float('inf')
            for node, distance in distances.items():
                if node not in visited and distance < min_distance:
                    min_distance = distance
                    next_node = node
            current = next_node

        return distances[end]

if __name__ == "__main__":
    g = Graph()
    print("MENU\nEnter an edge [Format Node Vertice Weight]\nor\nType done to finish")
    while True:
        edge_input = input("Enter Input: ")
        if edge_input.lower() == "done":
            break
        u, v, weight = map(int, edge_input.split())
        g.add_edge(u, v, weight)

    print("The graph is ---->")
    print("\n" + g.display() + "\n")

    start_node = int(input("Enter starting node: "))
    end_node = int(input("Enter ending node: "))

    cost = g.calculate_cost(start_node, end_node)
    if cost == float('inf'):
        print("There is no path between the start and end nodes.")
    else: 
        print(f"Cost from {start_node} to {end_node}: {cost}") 
