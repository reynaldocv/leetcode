# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums) 
        
        left = [num for num in nums]
        right = [num for num in nums]
        
        for i in range(1, n):
            left[i] = max(left[i], left[i - 1])
            
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i], right[i + 1])
            
        for i in range(n - 1):
            if left[i] <= right[i + 1]:
                return i + 1
            
        return -1
