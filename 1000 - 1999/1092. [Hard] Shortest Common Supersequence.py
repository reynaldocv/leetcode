# https://leetcode.com/problems/shortest-common-supersequence/

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        dp = [[(0, "-") for _ in range(n + 1)] for _ in range(m + 1)]
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1][0] + 1, "*")
                
                else: 
                    dp[i][j] = max((dp[i][j - 1][0], "-"), (dp[i - 1][j][0], "+"))
                    
        (x, y) = (m, n)
        
        common = ""
        
        while x > 0 and y > 0:                         
            (_, action) = dp[x][y]
            
            if action == "*":
                common = str1[x - 1] + common
                
                x -= 1 
                y -= 1 
                
            elif action == "-":
                common = str2[y - 1] + common
                
                y -= 1 
                
            else: 
                common = str1[x - 1] + common
                
                x -= 1 
        
        return str1[: x] + str2[: y] + common
         
                
