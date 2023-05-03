# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache        
        def helper(i):
            if i == n: 
                return 1 
            
            elif i > n: 
                return 0 
            
            else: 
                ans = 0                 
                tmp = ""
                
                for j in range(i, min(i + 2, n)):
                    tmp += s[j]
                    
                    if tmp in seen: 
                       ans += helper(j + 1)
                        
                return ans 
            
        n = len(s)
        
        seen = [word for word in wordDict]
        
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
        
         
