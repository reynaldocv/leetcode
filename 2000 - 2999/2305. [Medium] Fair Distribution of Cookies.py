# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:        
        @cache
        def helper(mask, k):
            if mask == 0: 
                return 0 
            
            if k == 0: 
                return inf
            
            ans = inf 
            
            orig = mask 
            
            while mask: 
                mask = orig & (mask - 1)
                amt = sum(cookies[i] for i in range(n) if (orig ^ mask) & 1 << i)
                ans = min(ans, max(amt, helper(mask, k - 1)))
            
            return ans 
        
        n = len(cookies)
                
        return helper((1 << n) - 1, k)
