# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        l = len(s) 
        
        seen = set()
        
        for i in range(l):
            num = 0
            
            for j in range(i, min(i + min(n, 32), l)):
                num = 2*num + int(s[j])
                
                if num != 0 and num <= n:                
                    seen.add(num)
              
        return len(seen) == n
