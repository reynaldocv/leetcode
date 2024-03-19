# https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def helper(start):
            if start == n:
                return 0 
            
            else: 
                ans = n - start
                
                for i in range(start + 1, n + 1):
                    tmp = s[start: i]
                    
                    if tmp == tmp[:: -1]:
                        ans = min(ans, 1 + helper(i))
                        
                return ans 
            
        n = len(s)
            
        return helper(0) - 1
        
            
        
