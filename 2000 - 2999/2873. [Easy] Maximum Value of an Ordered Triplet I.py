# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0 
        
        for (i, numA) in enumerate(nums):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    numB = nums[j]
                    numC = nums[k]
                    
                    ans = max(ans, (numA - numB)*numC)
                    
        return ans 
                    
