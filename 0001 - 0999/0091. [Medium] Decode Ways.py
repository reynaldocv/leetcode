# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def helper(string):
            n = len(string)
            if n == 0: 
                return 1 
            else: 
                ans = 0 
                for i in range(1, min(n + 1, 3)):
                    val = string[: i]
                    if val in seen: 
                        ans += helper(string[i: ])
                        
                return ans 
                
        seen = {str(i) for i in range(1, 27)}
        
        return helper(s)
                
                
