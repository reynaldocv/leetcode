# https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:        
        common = nums[0]
        
        for num in nums:
            common = gcd(common, num)
            
        return True if common == 1 else False
