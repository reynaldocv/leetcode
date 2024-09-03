# https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:        
        @cache
        def helper(idx, seen):
            if idx == l: 
                return 0 
            
            else: 
                ans = 0
                
                for i in range(idx, l):
                    (value, ith) = arr[i]
                    
                    if (seen >> ith) & 1 == 0: 
                        ans = max(ans, value + helper(nextIndex[value], seen ^ (2**ith)))
                        
                return ans 
            
        m, n = len(grid), len(grid[0])
        
        arr = []
        
        for i in range(m):
            for j in range(n):
                arr.append((grid[i][j], i))
                
        arr.sort(key = lambda item: -item[0])
        
        nextIndex = {}
        
        l = last = len(arr)
        
        for i in range(l - 1, -1, -1):
            value = arr[i][0]
            
            if value not in nextIndex: 
                nextIndex[value] = last
                
            last = i      
        
        return helper(0, 0)

