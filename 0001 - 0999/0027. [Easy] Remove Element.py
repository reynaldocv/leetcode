# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n, j = len(nums), 0
        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
            
            
        
