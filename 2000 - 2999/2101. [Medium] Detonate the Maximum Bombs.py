# https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:        
        def helper(u):
            seen = {u}
            stack = [u]
            
            while stack: 
                u = stack.pop()
            
                for v in graph[u]:
                    if v not in seen:                 
                        seen.add(v)
                        
                        stack.append(v)
            
            return len(seen)
        
        n = len(bombs)
        
        graph = defaultdict(lambda: [])
        
        for (i, (x, y, radius)) in enumerate(bombs):
            for (j, (r, s, _)) in enumerate(bombs):
                if i != j:
                    if (x - r)**2 + (y - s)**2 <= radius**2:
                        graph[i].append(j)
        
        ans = 0 
        for i in range(n):
            ans = max(ans, helper(i))
            
        return ans   
                
