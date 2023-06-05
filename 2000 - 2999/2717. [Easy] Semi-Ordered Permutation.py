# https://leetcode.com/problems/semi-ordered-permutation/

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums) 
        
        idx1 = 0 
        idxN = 0 
        
        for (i, num) in enumerate(nums):
            if num == 1: 
                idx1 = i 
                
            elif num == n: 
                idxN = i 
                
        if idx1 < idxN: 
            return idx1 + (n - 1 - idxN)
        
        else: 
            return idx1 - 1 +  (n - 1 - idxN)
        
        
        
