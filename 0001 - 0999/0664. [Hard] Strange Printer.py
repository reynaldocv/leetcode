# https://leetcode.com/problems/strange-printer/

class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def helper(start, end):
            if start == end: 
                return 0 
            else: 
                ans = 1 + helper(start + 1, end)
                for mid in range(start + 1, end):
                    if s[start] == s[mid]:
                        ans = min(ans, helper(start, mid) + helper(mid + 1, end))
                    
                return ans 
            
        s = "".join(char for (i, char) in enumerate(s) if i == 0 or s[i - 1] != char)
                
        n = len(s)
        
        return helper(0, n)
        
