# https://leetcode.com/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:        
        n = len(nums)
        
        non_increasing = [1 for _ in range(n)]
        non_decreasing = [1 for _ in range(n)]

        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                non_increasing[i] = non_increasing[i-1] + 1
                
        for i in range(n-2, 0, -1):
            if nums[i+1] >= nums[i]:
                non_decreasing[i] = non_decreasing[i+1] + 1
        
        ans = []

        for i in range(k, n - k):
            if non_increasing[i - 1] >= k and non_decreasing[i + 1] >= k:
                ans.append(i)
                
        return ans 
