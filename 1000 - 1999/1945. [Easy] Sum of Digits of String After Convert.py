# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def helper(word):
            ans = 0
            
            for char in word:
                ans += int(char)
                
            return str(ans)
        
        index = {chr(ord("a") + i): str(i + 1) for i in range(26)}
        
        ans = "" 
        
        for char in s: 
            ans += index[char]
          
        for _ in range(k):
            ans = helper(ans)
            
        return int(ans)
