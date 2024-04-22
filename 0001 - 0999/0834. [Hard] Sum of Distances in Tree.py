# https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def helper(parent, u):
            for v in graph[u]:
                if v != parent: 
                    helper(u, v)
                    
                    count[u] += count[v]
                    ans[u] += ans[v] + count[v]
        
        def collaborate(parent, u):
            for v in graph[u]:
                if v != parent: 
                    ans[v] = ans[u] - count[v] + n - count[v]
                    
                    collaborate(u, v)

        graph = {i: [] for i in range(n)}
        
        for (x, y) in edges: 
            graph[x].append(y)
            graph[y].append(x)
        
        count = [1 for _ in range(n)]
        ans = [0 for _ in range(n)]
        
        helper(None, 0)
        collaborate(None, 0)
        
        return ans
            
        
        
