# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        right = [num for num in nums]
        
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i], right[i + 1])
            
        left = nums[0]
        for i in range(n -1):
            if left <= right[i + 1]:
                return i + 1
            
            left = max(left, nums[i])
            
