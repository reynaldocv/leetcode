# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumEven = 0 
        for num in nums: 
            if num % 2 == 0: 
                sumEven += num 
                         
        ans = []        
        
        for (value, i) in queries:
            if nums[i] % 2 == 0: 
                sumEven -= nums[i] 
           
            nums[i] += value
            
            if nums[i] % 2 == 0: 
                sumEven += nums[i] 
                
            ans.append(sumEven)
            
        return ans 
            
            
