# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [1 for _ in range(n)]
        
        stack = []
        
        for (ith, num) in enumerate(nums):
            while stack and stack[-1][1] <= num: 
                (start, value) = stack.pop() 
                
                if value == num: 
                    dp[ith] = dp[start] + 1
                    
                    break 
                    
            stack.append((ith, num))
            
        return sum(dp)
