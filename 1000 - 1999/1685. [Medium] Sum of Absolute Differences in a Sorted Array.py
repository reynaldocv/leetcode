# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        left = 0 
        right = sum(nums)
        
        ans = []
        
        for (i, num) in enumerate(nums): 
            l = num*i - left
            r = right - num*(n - i)
            
            ans.append(l + r)
            
            left += num 
            right -= num 
            
        return ans 
            
            
            
        
