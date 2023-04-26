# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def helper(a, b):
            if a % b == 0: 
                return b 
            
            else: 
                return helper(b, a % b)
            
        minNum = inf 
        maxNum = 0 
        
        for num in nums: 
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
            
        return helper(minNum, maxNum)
        
