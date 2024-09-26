# https://leetcode.com/problems/maximum-multiplication-score/

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        
        last = a[-1]
        
        dp = [num*last for num in b]
        
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i], dp[i + 1])
            
        for (ith, num) in enumerate(a[: -1][:: -1]):
            newDp = [-inf for _ in range(n)]
            
            for j in range(n - 2 - ith, -1, -1):
                newDp[j] = num*b[j] + dp[j + 1]
                
            for i in range(n - 2, -1, -1):
                newDp[i] = max(newDp[i], newDp[i + 1])
                
            dp = newDp
                        
        return dp[0]
                    
