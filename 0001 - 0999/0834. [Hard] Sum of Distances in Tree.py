# https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent: 
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent: 
                    ans[child] = ans[node] - count[child] + n - count[child]
                    dfs2(child, node)

        graph = {node: [] for node in range(n)}
        for (x, y) in edges: 
            graph[x], graph[y] = graph.get(x, []), graph.get(y, [])
            graph[x].append(y)
            graph[y].append(x)
        
        count = [1]*n
        ans = [0]*n
        
        dfs(0, None)
        dfs2(0, None)
        
        return ans
