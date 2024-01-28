# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        arr = []
        
        for num in nums[1: ]: 
            insort(arr, num)
            
            arr = arr[: 2]
            
        return nums[0] + sum(arr)
        
