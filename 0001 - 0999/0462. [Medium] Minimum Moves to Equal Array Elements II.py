# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        ans = 0 
        for num in nums: 
            ans += abs(num - median)
            
        return ans

      
