# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution:
    def minFlips(self, s: str) -> int:
        def helper(string, val):
            ans = flips = 0 
            val2 = val
            
            for char in string:
                if int(char) != val:
                    flips += 1 
                    
                val = 1 - val
            
            ans = flips
            
            for char in string: 
                if int(char) != val:
                    flips += 1 
                    
                if int(char) != val2: 
                    flips -= 1 
                    
                ans = min(ans, flips)
                    
                val, val2 = 1 - val, 1 - val2
                
            return ans 
        
        return min(helper(s, 0), helper(s, 1))
