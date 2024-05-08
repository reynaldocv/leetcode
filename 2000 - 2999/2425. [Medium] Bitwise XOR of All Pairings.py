# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        num1 = 0 
        num2 = 0 
        
        for num in nums1: 
            num1 ^= num
            
        for num in nums2: 
            num2 ^= num 
            
        if m % 2 == n % 2:
            if m % 2 == 0: 
                return 0 
            
            else: 
                return num1^num2
            
        else: 
            if m % 2 == 0: 
                return num1
            
            else: 
                return num2
            
            
        
