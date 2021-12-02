# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(1, 1) for _ in range(n)]
        
        for i in range(1, n):
            ans = 0
            count = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] > ans: 
                        ans = dp[j][0]
                        count = dp[j][1]
                    elif dp[j][0] == ans:
                        count += dp[j][1]
            if count != 0:
                dp[i] = (ans + 1, count)
        

        maxValue = 0 
        ans = 0
        for (val, count) in dp: 
            if maxValue < val: 
                maxValue = val
                ans = count
            elif maxValue == val: 
                ans += count
                
        return ans
