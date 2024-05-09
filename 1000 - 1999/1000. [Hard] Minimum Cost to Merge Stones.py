# https://leetcode.com/problems/minimum-cost-to-merge-stones/

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        @cache 
        def helper(start, end):
            if end - start < k: 
                return 0 
            
            else: 
                ans = inf 
                
                for mid in range(start + 1, end, k - 1):
                    ans = min(ans, helper(start, mid) + helper(mid, end))

                if (end - start - 1) % (k - 1) == 0: 
                    ans += dp[end] - dp[start]

                return ans 

        n = len(stones)
        
        if (n - 1) % (k - 1) != 0: 
            return -1
        
        dp = [0]
        
        for stone in stones: 
            dp.append(dp[-1] + stone)
            
        ans = helper(0, n)
        
        return -1 if ans == inf else ans 
            
        
