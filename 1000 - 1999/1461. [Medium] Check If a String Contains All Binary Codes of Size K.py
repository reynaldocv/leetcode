# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        prev = s[: k - 1]
        
        seen = set()
        
        for char in s[k - 1: ]:
            prev += char 
            
            seen.add(prev)
            
            prev = prev[1: ]
            
        return len(seen) == 2**k
        
        
        
