# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def helper(arr):            
            if arr[0] < 0: 
                return n
            
            start = 0     
            end = n 
            
            while end - start > 1: 
                mid = (end + start)//2
                if arr[mid] < 0: 
                    end = mid
                else: 
                    start = mid
                    
            return n - 1 - start
            
        m, n = len(grid), len(grid[0])
        
        ans = 0 
        for i in range(m):
            ans += helper(grid[i])
            
        return ans 
        
