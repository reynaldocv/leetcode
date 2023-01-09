# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        neg = bisect_left(nums, 0)
        
        pos = n - bisect_right(nums, 0)
        
        return max(neg, pos)
        
