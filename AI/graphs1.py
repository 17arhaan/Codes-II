class graph:
    def __init__ (self,vertices):
        self.vertices = vertices
        self.adj_list = {v : [] for v in range (vertices)}
        self.adj_matrix = [[0] * vertices for _ in range (vertices)]

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        self.adj_matrix[v][u]
        self.adj_matrix[u][v]
        
        