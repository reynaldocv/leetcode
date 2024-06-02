# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        zeros = 0 
        
        maxElem = zeros + ones
        
        for num in nums:
            if num == 0: 
                zeros += 1 
                
            else: 
                ones -=1 
                
            maxElem = max(maxElem, zeros + ones)
            
        ans = []
        
        ones = sum(nums)
        zeros = 0 
        
        if ones + zeros == maxElem: 
            ans.append(0)
            
        for (ith, num) in enumerate(nums, 1): 
            if num == 0: 
                zeros += 1 
                
            else: 
                ones -=1 
                
            if zeros + ones == maxElem: 
                ans.append(ith)
                                  
        return ans             
        
    
        
        
