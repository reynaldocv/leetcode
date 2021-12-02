# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)        
        auxXor = 0
        for i in range(n):
            auxXor = nums[i] ^ auxXor
        
        setbit = auxXor & (~auxXor + 1)
        
        a, b = 0, 0
        for i in range(n):
            if (nums[i] & setbit):
                a = a^nums[i]
            else:
                b = b^nums[i]
        
        return [a, b]
