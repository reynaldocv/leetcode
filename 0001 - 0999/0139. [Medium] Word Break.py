# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache 
        def helper(i):
            if i >= n: 
                return True 
            
            else: 
                tmp = ""
                
                for j in range(i, n):
                    tmp += s[j]
                    
                    if tmp in seen and helper(j + 1):
                        return True 
                    
                return False 
            
        n = len(s)
        
        seen = {word for word in wordDict}
        
        return helper(0)
                
