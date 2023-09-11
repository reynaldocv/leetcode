# https://leetcode.com/problems/repeated-string-match/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def helper(i):
            ans = 1 
            
            j = 0 
            
            while j < n: 
                if a[i] != b[j]:
                    return -1 
                
                i += 1 
                j += 1 
                
                if i == m: 
                    if j != n: 
                        ans += 1 
                        
                    i = 0 
                        
            return ans             
            
        m, n = len(a), len(b)
        
        for i in range(m):
            tmp = helper(i)
            
            if tmp > -1:
                return tmp 
            
        return -1
        
