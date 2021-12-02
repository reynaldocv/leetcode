# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1, n + 1//2):
            if n % i == 0:
                q = n // i
                aux = s[:i]*q
                if aux == s:
                    return True
        return False
        
            
        
        
