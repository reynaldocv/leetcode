# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while (end - start > 1):
            m = (end + start)//2
            if nums[m] > target:
                end = m
            else: 
                start = m
        if nums[start] == target:
            return start
        else:
            return -1
        
