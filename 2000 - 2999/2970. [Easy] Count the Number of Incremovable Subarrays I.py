# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0 
        
        for i in range(n):
            for j in range(i, n):
                _tmp = nums[: i] + nums[j + 1: ]
                
                if _tmp == sorted(_tmp):
                    if len(_tmp) == len(set(_tmp)):
                        ans += 1 
                    
        return ans 
