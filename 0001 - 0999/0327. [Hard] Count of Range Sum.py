# https://leetcode.com/problems/count-of-range-sum/

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ans = prefix = 0 
        arr = [0]
        for num in nums: 
            prefix += num
            
            start = bisect_left(arr, prefix - upper)
            end = bisect_right(arr, prefix - lower)           
            
            ans += end - start 
            insort(arr, prefix)
            
        return ans 
