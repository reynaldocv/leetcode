# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        aux = inf
        idx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != aux:
                nums[idx] = nums[i]
                aux = nums[i]
                idx += 1
        return idx
        
