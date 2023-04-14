# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        
        i, j = 0, 1
        
        ans = n
        
        while j < n: 
            if nums[i] == nums[j]:
                j += 1 
                
            else: 
                ans -= 2 
                
                i = j + 1
                j += 1 
                
        return ans 
        
