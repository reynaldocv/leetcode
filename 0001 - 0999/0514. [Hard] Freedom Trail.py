# https://leetcode.com/problems/freedom-trail/

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def helper(ptr, idx):
            if idx == m:
                return 0
            else: 
                ans = inf
                for j in graph[key[idx]]:
                    aux = min(abs(ptr - j), abs(abs(ptr - j) - n))
                    
                    ans = min(ans, helper(j, idx + 1) + aux)
                    
                return ans
            
        n, m = len(ring), len(key)
        
        graph = defaultdict(lambda: [])
        
        for i in range(n):
            graph[ring[i]].append(i)
            
        return helper(0, 0) + m
        
