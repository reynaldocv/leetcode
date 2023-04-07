# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        even = 0 
        odd = 1 
        
        ans = [0 for _ in range(n)]
        
        for num in nums:
            if num % 2 == 1: 
                ans[odd] = num 
                
                odd += 2 
                
            else: 
                ans[even] = num 
                
                even += 2 
                
        return ans 
                
        
