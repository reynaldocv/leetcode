# https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr) 
        
        dp = defaultdict(lambda: 0)
         
        for (i, num) in enumerate(arr):
            minNum = 0
            tmp = 0
            
            for j in range(i, max(i - k, -1), -1):
                minNum = max(minNum, arr[j])
                
                tmp = max(tmp, minNum*(i - j + 1) + dp[j - 1])
                
            dp[i] = tmp
            
        return dp[n - 1]
            
                
