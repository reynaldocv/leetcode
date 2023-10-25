# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort() 
        
        ans = 0 
        
        limit = nums[0] - 1
        
        for num in nums: 
            if limit < num: 
                limit = num 
                
            else: 
                limit += 1 
                
                ans += limit - num 
                
        return ans 
        
