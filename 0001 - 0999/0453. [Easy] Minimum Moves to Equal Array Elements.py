# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ = min(nums)
        ans = 0
        for num in nums:
            ans += num - min_
        return ans
        
        
            
            
        

