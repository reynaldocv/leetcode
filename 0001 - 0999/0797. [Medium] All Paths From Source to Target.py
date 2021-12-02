# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def DFS(way, graph, end):         
            lastElem = way[len(way) - 1]
            if lastElem == end: 
                self.ans.append(list(way))
            else:
                for elem in graph[lastElem]:
                    way.append(elem)
                    DFS(way, graph, end)
                    way.pop()
        
        self.ans = []
        DFS([0], graph, len(graph) - 1)
        
        return self.ans
                
        
