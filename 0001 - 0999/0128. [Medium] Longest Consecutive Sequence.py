# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 0)
        
        for num in nums: 
            if dp[num] == 0: 
                left = dp[num - 1]
                right = dp[num + 1]
                
                total = left + right + 1
                
                dp[num - left] = total 
                dp[num + right] = total 
                
                if dp[num] == 0: 
                    dp[num] = 1
                
        ans = 0 

        for key in dp:
            ans = max(ans, dp[key])
        
        return ans 
        
        
            
