# https://leetcode.com/problems/points-that-intersect-with-cars/submissions/

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort() 
        
        last = -inf         
        ans = 0 
        
        for (start, end) in nums: 
            if last < start: 
                ans += end - start + 1
                
            elif end > last:
                ans += end - last 
                
            last = max(last, end)
            
        return ans 
