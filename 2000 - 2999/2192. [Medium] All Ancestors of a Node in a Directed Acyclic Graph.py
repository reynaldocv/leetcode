# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        @cache
        def helper(u):
            ans = set()
            
            for v in graph[u]:
                ans.add(v)
                
                for elem in helper(v):
                    ans.add(elem)
                
            return sorted(ans) 
        
        graph = defaultdict(lambda: [])
        
        for (u, v) in edges:
            graph[v].append(u)
        
        ans = []
        
        for i in range(n):            
            ans.append(helper(i))
            
        return ans
