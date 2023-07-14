# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = {}
        
        for i in range(26):
            lower = chr(ord("a") + i)
            upper = chr(ord("A") + i)
            
            letters[lower] = [lower, upper]
            letters[upper] = [lower, upper]
            
        for i in range(10):
            letters[str(i)] = [str(i)]
            
        ans = [""]
        
        for char in s: 
            tmp = []
                
            for word in ans: 
                for letter in letters[char]:
                    tmp.append(word + letter)
                
            ans = tmp 
            
        return ans
                
class Solution2:
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
        
            
        
        
        
        
        
