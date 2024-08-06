# https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def helper(u, graph):
            ans = -1
            last = -1 
            
            stack = [u]
            seen = {u}
            
            while stack: 
                newStack = []
                
                for u in stack:                 
                    for v in graph[u]:
                        if v not in seen: 
                            newStack.append(v)
                            seen.add(v)

                            last = v 

                ans += 1 
                stack = newStack 
                
            return (ans, last)
        
        def collaborator(edges):
            graph = defaultdict(lambda: [])
            
            for (u, v) in edges: 
                graph[u].append(v)
                graph[v].append(u)
                
            (_, u) = helper(0, graph)
            (ans, _) = helper(u, graph)
            
            return ans 
        
        diameter1 = collaborator(edges1)
        diameter2 = collaborator(edges2)
        
        return max(diameter1, diameter2, (diameter1 + 1)//2 + (diameter2 + 1)//2 + 1)

                        
            
        
