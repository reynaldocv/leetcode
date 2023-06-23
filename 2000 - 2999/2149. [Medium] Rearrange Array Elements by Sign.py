# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        posIdx = 0 
        negIdx = 1 
        
        ans = [0 for _ in range(n)]
        
        for num in nums: 
            if num < 0: 
                ans[negIdx] = num 
                
                negIdx += 2 
                
            else: 
                ans[posIdx] = num 
                
                posIdx += 2 
                
        return ans 
        
        
        
