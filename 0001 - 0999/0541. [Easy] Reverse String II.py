# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        
        ans = ""
        count = 0 
        for i in range(0, n, k):
            if count == 0: 
                ans += s[i: i + k][:: -1]
            else:
                ans += s[i: i + k]
            
            count = 1 - count
                
        return ans 
        
