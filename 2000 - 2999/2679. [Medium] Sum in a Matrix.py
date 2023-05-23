# https://leetcode.com/problems/sum-in-a-matrix/

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        
        for row in nums:
            row.sort(key = lambda item: -item) 
            
        ans = 0 
        
        for j in range(n):
            maxElem = nums[0][j]
            
            for i in range(1, m):
                maxElem = max(maxElem, nums[i][j])
                
            ans += maxElem
    
        return ans 
