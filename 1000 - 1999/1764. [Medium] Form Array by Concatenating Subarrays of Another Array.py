# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        
        for group in groups: 
            for j in range(i, n):
                if nums[j: j + len(group)] == group: 
                    i = j + len(group)
                    break
                    
            else: 
                return False
        
        return True
