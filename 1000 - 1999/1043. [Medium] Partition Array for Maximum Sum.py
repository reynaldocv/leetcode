# https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*n
        
        for (i, num) in enumerate(arr):
            maxElem = 0 
            ans = 0 
            for j in range(i, max(-1, i - k), -1):
                maxElem = max(maxElem, arr[j])
                prev = 0 if j == 0 else dp[j - 1]
                ans = max(ans, prev + maxElem*(i + 1 - j))
                
            dp[i] = ans
            
        return dp[-1]
                
            
                
