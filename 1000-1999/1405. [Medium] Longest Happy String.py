# https://leetcode.com/problems/longest-happy-string/

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def helper(letter):
            ans = (0, "$")
            for key in seen: 
                if key != letter: 
                    ans = max(ans, (seen[key], key))
                    
            return ans[1]
        
        seen = {}
        if a >= 1: 
            seen["a"] = a
        if b >= 1: 
            seen["b"] = b
        if c >= 1: 
            seen["c"] = c
        
        
        prev = "$"
        cnt = 1
        
        ans = ""
        while seen:             
            if cnt == 1:
                letter = helper("$")
            elif cnt == 2:
                letter = helper(prev)
                cnt = 1
            if letter == "$":
                break
            
            cnt = cnt + 1 if prev == letter else cnt
            
            if letter != "$":
                seen[letter] -= 1                
                if seen[letter] == 0: 
                    seen.pop(letter)
            
            prev = letter
            ans += letter
        
        return ans
