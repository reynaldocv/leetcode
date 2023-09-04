# https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution:
    def minimumOperations(self, num: str) -> int:
        def helper(pattern, word):
            n = len(word)
            
            start = 0 
            
            for (i, char) in enumerate(word): 
                if pattern[start] == char: 
                    start += 1 
                    
                if start == 2: 
                    return i - 1
            
            return inf 
        
        num = num[:: -1]
        
        ans = sum(1 for char in num if char != "0")
        
        ans = min(ans, helper("52", num))
        ans = min(ans, helper("05", num))
        ans = min(ans, helper("57", num))
        ans = min(ans, helper("00", num))
        
        return ans 
        
                    
