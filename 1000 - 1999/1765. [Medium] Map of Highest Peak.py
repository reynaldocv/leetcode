# https://leetcode.com/problems/map-of-highest-peak/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        
        stack, seen = [], {}
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    stack.append((i, j))
                    seen[(i, j)] = True
        
        val = 0
        ans = [[0 for j in range(n)] for i in range(m)]
        
        while stack: 
            newStack = []
            for (x, y) in stack: 
                ans[x][y] = val
                for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < m and 0 <= s < n: 
                        if (r, s) not in seen: 
                            newStack.append((r, s))
                            seen[(r, s)] = True
            
            stack = newStack[:]                            
            val += 1
            
        return ans
                        
                        
                    
                
            
        
