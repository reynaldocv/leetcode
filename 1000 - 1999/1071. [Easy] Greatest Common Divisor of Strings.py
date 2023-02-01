# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        if m < n: 
            m, n = n, m 
            str1, str2 = str2, str1
        
        for i in range(n, 0, -1):
            if n % i == 0: 
                ans = str2[: i]
                
                if str2 == ans*(n//i) and str1 == ans*(m//i):
                    return ans 
                
        return ""
        
