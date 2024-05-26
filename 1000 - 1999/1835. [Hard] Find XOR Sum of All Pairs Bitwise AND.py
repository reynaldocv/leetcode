# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        prev1 = 0 
        prev2 = 0 
        
        for num in arr1: 
            prev1 ^= num 
            
        for num in arr2: 
            prev2 ^= num 
            
        return prev1 & prev2
        
