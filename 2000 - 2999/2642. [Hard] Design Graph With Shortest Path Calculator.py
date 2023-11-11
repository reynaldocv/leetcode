# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.distance = [[inf for _ in range(n)] for _ in range(n)]
        
        for (u, v, cost) in edges: 
            self.distance[u][v] = cost
            
        for i in range(n):
            self.distance[i][i] = 0 
            
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.distance[j][k] = min(self.distance[j][k], self.distance[j][i] + self.distance[i][k])
                        
    def addEdge(self, edge: List[int]) -> None:
        n = len(self.distance)
        
        (u, v, cost) = edge
        
        for i in range(n):
            for j in range(n):
                self.distance[i][j] = min(self.distance[i][j], self.distance[i][u] + self.distance[v][j] + cost)
        
    def shortestPath(self, node1: int, node2: int) -> int:
        if self.distance[node1][node2] == inf:
            return -1 
        
        else: 
            return self.distance[node1][node2]
           
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
