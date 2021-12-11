# https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def distance(x, y, r, s):
            return (r - x)**2 + (s - y)**2
        
        def dfs(u):
            seen = {u: True}
            stack = [u]
            while stack: 
                u = stack.pop()
                for v in graph[u]:
                    if v not in seen: 
                        seen[v] = True
                        stack.append(v)
            
            return len(seen)
        
        n = len(bombs)
        
        graph = defaultdict(lambda: [])
        
        for (i, (x, y, radius)) in enumerate(bombs):
            aux = 1 
            for (j, (r, s, _)) in enumerate(bombs):
                if i != j:
                    if distance(x, y, r, s) <= radius**2:
                        graph[i].append(j)
        
        ans = 0 
        for i in range(n):
            ans = max(ans, dfs(i))
            
        return ans
                
