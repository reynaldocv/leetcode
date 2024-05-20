# https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def helper(x, jump, down):
            if x > k + 1: 
                return 0 
            
            ans = 0 
            
            if x == k: 
                ans += 1 
            
            ans += helper(x + pow(2, jump), jump + 1, False)
            
            if not down and x > 0: 
                ans += helper(x - 1, jump, True)
                
            return ans
        
        return helper(1, 0, False)
    
    
