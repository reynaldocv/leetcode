# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        tail = [nums[n - 1]]
        
        for i in range(n - 2, -1, -1):
            idx = bisect_left(tail, nums[i])
            counts[i] = idx
            tail.insert(idx, nums[i])
        
        return counts
        
