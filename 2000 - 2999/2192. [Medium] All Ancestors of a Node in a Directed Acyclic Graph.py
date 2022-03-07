# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        @cache
        def helper(u):
            ans = set()
            for v in graph[u]:
                ans.add(v)
                for w in helper(v):
                    ans.add(w)
            
            return sorted(ans)
            
        graph = defaultdict(lambda: [])
        for (a, b) in edges: 
            graph[b].append(a)
            
        origins = [i for i in range(n) if len(graph[i]) == 0]
        
        ans = []
        seen = {}
        
        for i in range(n):
            ans.append(helper(i))
        
        return ans 
