# https://leetcode.com/problems/binary-trees-with-factors/

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        n = len(arr)
        
        arr.sort()
        index = {num: i for (i, num) in enumerate(arr)}
        
        dp = [1 for i in range(n)]
        
        for (i, numA) in enumerate(arr):
            for (j, numB) in enumerate(arr[:i]):
                if numA % numB == 0: 
                    numC = numA//numB
                    if numC in index: 
                        dp[i] += dp[j]*dp[index[numC]]
                        dp[i] %= MOD
    
        return sum(dp) % MOD
        
