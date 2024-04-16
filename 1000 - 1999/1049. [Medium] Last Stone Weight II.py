# https://leetcode.com/problems/last-stone-weight-ii/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache 
        def helper(idx, sum1, sum2):
            if idx == n: 
                return abs(sum1 - sum2)
            else: 
                val1 = helper(idx + 1, sum1 + stones[idx], sum2)
                val2 = helper(idx + 1, sum1, sum2 + stones[idx])
                
                return min(val1, val2)
            
        n = len(stones)
        
        return helper(0, 0, 0)

class Solution2:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        aSum = sum(stones)
        
        limit = aSum//2 
        
        dp = [1] + [0 for _ in range(limit)]
        
        partial = 0 
        
        for stone in stones: 
            for num in range(limit, stone - 1, -1):
                dp[num] += dp[num - stone]
                
                if dp[num] > 0: 
                    partial = max(partial, num)
                    
        return (aSum - partial) - partial
                
        
        
