# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        aux, n = -inf, len(nums)
        for i in range(n):
            if aux != nums[i]:
                x = n - i                
                if x == nums[i] or (aux < x <= nums[i] and x not in nums):
                    return x
                aux = nums[i]
        return -1
                    
                    
