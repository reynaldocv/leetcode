# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip = False 
        
        ans = 0
        
        for num in nums: 
            if flip == 0: 
                if num != 1: 
                    ans += 1 
                    
                    flip = not flip 
                    
            else: 
                if num != 0: 
                    ans += 1
                    
                    flip = not flip
                    
        return ans 
            
