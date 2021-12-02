# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return False
        
        minimum = [num for num in nums]
        maximum = [num for num in nums]
        
        for i in range(1, n):
            minimum[i] = min(minimum[i - 1], minimum[i])
        
        for i in range(n - 2, -1, -1):
            maximum[i] = max(maximum[i], maximum[i + 1])
            
        for i in range(1, n - 1):
            if minimum[i - 1] < nums[i] < maximum[i + 1]:
                return True
        
        return False
            
        
        
