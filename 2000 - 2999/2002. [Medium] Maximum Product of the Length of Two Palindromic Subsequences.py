# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

class Solution1:
    def maxProduct(self, s: str) -> int:
        @cache
        def helper(first, second, word):
            nonlocal ans 
            
            if word == "":
                ans = max(ans, collaborator(first)*collaborator(second))
                
            else: 
                helper(first + word[0], second, word[1: ])
                helper(first, second + word[0], word[1: ])
              
        @cache
        def collaborator(word):
            if word == "":
                return 0 
            
            n = len(word)
            
            dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
            
            tmp = word[:: -1]
            
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if word[i - 1] == tmp[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                        
                    else: 
                        dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
                        
            return dp[-1][-1]
                        
        ans = 0 
        
        helper("", "", s)
        
        return ans 

class Solution2:
    def maxProduct(self, s: str) -> int:
        @cache 
        def helper(first, second, i):
            nonlocal ans 
            
            if i == n: 
                if first == first[:: -1] and second == second[:: -1]:
                    ans = max(ans, len(first)*len(second))
                    
            else: 
                helper(first + s[i], second, i + 1)
                helper(first, second + s[i], i + 1)
                helper(first, second, i + 1)
        
        n = len(s)
        
        ans = 0 
        
        helper("", "", 0)
        
        return ans 
