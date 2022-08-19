# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def helper(arr):
            start = -1            
            end = m 
            
            while end - start > 1: 
                mid = (end + start)//2
                
                if arr[mid] >= 0:
                    start = mid 
                else: 
                    end = mid 
            
            return m - end
        
        ans = 0 
        
        m = len(grid[0])
        
        for row in grid: 
            ans += helper(row)
            
        return ans 
                    
        
