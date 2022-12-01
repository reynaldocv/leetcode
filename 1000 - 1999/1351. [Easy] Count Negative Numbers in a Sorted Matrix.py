# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def helper(arr):
            n = len(arr)
            
            start = -1
            end = n 
            
            while end - start > 1: 
                mid = (end + start)//2
                
                if arr[mid] >= 0:
                    start = mid 
                else: 
                    end = mid 
                    
            return n - end
        
        ans = 0 
        
        for arr in grid: 
            ans += helper(arr)
            
        return ans 
                    
class Solution2:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        stack = [(m - 1, n - 1)] if grid[-1][-1] < 0 else []
        seen = {(m - 1, n - 1)} if grid[-1][-1] < 0 else {}
        
        while stack: 
            (x, y) = stack.pop() 
            
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s
                
                if 0 <= p < m and 0 <= q < n: 
                    if (p, q) not in seen and grid[p][q] < 0: 
                        seen.add((p, q))
                        stack.append((p, q))
                        
        return len(seen)  
