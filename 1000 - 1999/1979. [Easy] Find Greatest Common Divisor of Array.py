# 1979. Find Greatest Common Divisor of Array

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def mcd(a, b):
            if b == 0: 
                return a
            else: 
                return mcd(b, a % b)
        
        n = len(nums)
        minElem = nums[0]
        maxElem = nums[0]
        for i in range(n):
            minElem = min(minElem, nums[i])
            maxElem = max(maxElem, nums[i])
        
        return mcd(minElem, maxElem)
