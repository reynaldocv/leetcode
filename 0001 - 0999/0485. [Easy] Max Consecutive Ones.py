# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        counter, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = max(ans, counter)
                counter = 0
            else: 
                counter += 1
        ans = max(ans, counter)
        return ans        
        
