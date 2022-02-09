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
