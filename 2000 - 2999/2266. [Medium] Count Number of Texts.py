# https://leetcode.com/problems/count-number-of-texts/

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        @cache
        def helper(n):
            ans = [0, 1, 2, 4]
            if n <= 3: 
                return ans[n]
            else: 
                return helper(n - 1) + helper(n - 2) + helper(n - 3)
            
        @cache
        def collaborator(n):
            ans = [0, 1, 2, 4, 8]
            if n <= 4: 
                return ans[n]
            else: 
                return collaborator(n - 1) + collaborator(n - 2) + collaborator(n - 3) + collaborator(n - 4)
            
        MOD = 10**9 + 7a
        prev = "$"
        cnt = 1 
        ans = 1 
        for char in pressedKeys + "$": 
            if prev != char: 
                if prev == "7" or prev == "9":
                    ans = (ans * collaborator(cnt)) % MOD
                else: 
                    ans = (ans * helper(cnt)) % MOD
                    
                prev = char 
                cnt = 1 
            
            else: 
                cnt += 1 
                
        return ans 
                
                
                    
                
                    
                
            
