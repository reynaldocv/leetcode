# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def helper(times, aSum):
            if times == n: 
                if aSum == target: 
                    return 1
                else: 
                    return 0 
            else: 
                ans = 0
                for i in range(1, k + 1):
                    ans += helper(times + 1, aSum + i)
                    
                return ans
            
            return 0 
        
        MOD = 10**9 + 7
        
        if n*k < target:
            return 0 
        elif n*k == target:
            return 1
        
        return helper(0, 0) % MOD
                        
                    
