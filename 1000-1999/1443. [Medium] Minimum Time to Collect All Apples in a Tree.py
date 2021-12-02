# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def helper(u):
            if u != 0 and len(graph[u]) == 1:
                return (True, 0) if hasApple[u] else (False, 0)
            
            apples, ans = False, 0
            
            for v in graph[u]:                
                if v not in seen: 
                    seen[v] = True
                    apple, total = helper(v)
                    apples = apples or apple
                    ans += total + 2 if apple else 0 

            if not apples: 
                return (True, 0) if hasApple[u] else (False, 0)
            else: 
                return (True, ans)

        graph = [[] for _ in range(n)]
        for (u, v) in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        seen = {0: True}
        
        return helper(0)[1]
