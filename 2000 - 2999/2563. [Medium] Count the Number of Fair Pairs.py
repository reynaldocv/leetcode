# https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        arr = []
        
        ans = 0 
        
        for num in nums: 
            end = bisect_right(arr, upper - num)
            start = bisect_left(arr, lower - num)
            
            ans += end - start
            
            insort(arr, num)
            
        return ans 
            
            
            
