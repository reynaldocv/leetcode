# https://leetcode.com/problems/decode-ways-ii/

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache 
        def helper(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0 
            if i == n - 1: 
                return 9 if s[i] == "*" else 1
            if s[i] == "*":
                ans = 9*helper(i + 1)
                if s[i + 1] == "*": 
                    ans += 15*helper(i + 2)
                else: 
                    ans += helper(i + 2)
                    if s[i + 1] <= "6":
                        ans += helper(i + 2)
            
            else: 
                ans = helper(i + 1)
                if s[i + 1] == "*":
                    if s[i] == "1":
                        ans += 9*helper(i + 2)
                    elif s[i] == "2": 
                        ans += 6*helper(i + 2)
                elif int(s[i:i + 2]) <= 26: 
                    ans += helper(i + 2)
                    
            return ans % MOD
        
        MOD = 10**9 + 7
        n = len(s)
        
        return helper(0)
