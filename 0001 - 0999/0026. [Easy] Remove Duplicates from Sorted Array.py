# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -inf 
        
        idx = 0 
        
        for num in nums: 
            if num != prev: 
                nums[idx] = num 
                prev = num 
                idx += 1 
                
        return idx
