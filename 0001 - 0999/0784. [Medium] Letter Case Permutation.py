# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def recursive(newS, i):
            if i == n:
                ans.append(newS)
            elif s[i].isalpha(): 
                recursive(newS + s[i].upper(), i + 1)
                recursive(newS + s[i].lower(), i + 1)
            else: 
                recursive(newS + s[i], i + 1)
                
        n = len(s)
        ans = []
        recursive("", 0)
        
        return ans
        
            
        
        
        
        
        
