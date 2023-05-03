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
                
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, m = len(s), max(len(word) for word in wordDict)
        
        dp = [True] + [False for _ in range(n)]
        
        seen = [word for word in wordDict]
        
        for i in range(n + 1):
            if dp[i] == True: 
                tmp = ""
                
                for j in range(i, min(i + m, n)):
                    tmp += s[j]
                    
                    if tmp in seen: 
                        dp[j + 1] = True 

        return dp[-1]
        
