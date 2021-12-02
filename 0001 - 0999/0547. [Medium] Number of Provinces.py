# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def helper(v0):
            stack = [v0]
            seen[v0] = True
            while stack: 
                v0 = stack.pop()                
                for (v1, edge) in enumerate(isConnected[v0]):
                    if edge == 1 and v1 not in seen: 
                        seen[v1] = True
                        stack.append(v1)
                        
        seen = {}
        n = len(isConnected)
        ans = 0
        for v0 in range(n):
            if v0 not in seen: 
                helper(v0)
                ans += 1
                
        return ans
        
        
        
        
