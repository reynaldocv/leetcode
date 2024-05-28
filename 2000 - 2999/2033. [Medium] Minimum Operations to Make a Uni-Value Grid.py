# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        def helper(arr, value):
            ans = 0 
            
            for num in arr: 
                diff = abs(num - value)
                
                if diff % x == 0: 
                    ans += diff//x 
                    
                else: 
                    return inf 
                
            return ans 
            
        m, n = len(grid), len(grid[0])
        
        arr = [grid[i][j] for i in range(m) for j in range(n)]
        
        arr.sort() 
        
        if m*n % 2 == 1:
            ans = helper(arr, arr[m*n//2])
        
        else: 
            ans = min(helper(arr, arr[m*n//2]), helper(arr, arr[m*n//2 - 1]))
        
        return -1 if ans == inf else ans 
        
        
 
        
