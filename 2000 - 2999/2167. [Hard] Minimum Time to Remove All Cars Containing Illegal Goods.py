# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

class Solution:
    def minimumTime(self, s: str) -> int:
        def helper(string):
            ans = [i + 1 for i in range(n)]
        
            prev = 0
            for (i, char) in enumerate(string):
                if char == "1":
                    prev += 2
                    prev = ans[i] = min(ans[i], prev)
                else: 
                    ans[i] = ans[i - 1] if i > 0 else 0 
            
            return ans
        
        n = len(s)
        
        left = helper(s)
        right = helper(s[::-1])[::-1]  
                
        ans = inf
        for i in range(n + 1):
            l = 0 if i == 0 else left[i - 1]
            r = 0 if i == n else right[i]
            ans = min(ans, l + r)
            
        return ans
            
