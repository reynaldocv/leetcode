# https://leetcode.com/problems/maximum-score-of-a-good-subarray/

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        left = [-1 for _ in range(n)]
        right = [n for _ in range(n)]
        
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                left[stack.pop()] = i 
                
            stack.append(i)
            
        stack = []
        
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                right[stack.pop()] = i 
                
            stack.append(i)
            
        ans = 0 
        
        for i in range(n):
            if left[i] < k < right[i]: 
                ans = max(ans, nums[i]*(right[i] - left[i] - 1))
                
        return ans 
            
        
        
        
        
