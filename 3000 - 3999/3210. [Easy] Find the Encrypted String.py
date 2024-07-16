# https://leetcode.com/problems/find-the-encrypted-string/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
              
        k %= n
        
        return s[k: ] + s[: k]
        
