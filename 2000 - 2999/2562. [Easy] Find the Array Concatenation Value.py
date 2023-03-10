# https://leetcode.com/problems/find-the-array-concatenation-value/

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        
        start = 0 
        end = n - 1
        
        ans = 0
        
        while start < end: 
            ans += int(str(nums[start])+ str(nums[end]))
            
            start += 1 
            end -= 1 
            
        if start == end: 
            ans += int(nums[start])
            
        return ans 
            
            
