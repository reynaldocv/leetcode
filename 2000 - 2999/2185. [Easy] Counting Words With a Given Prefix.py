# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        
        ans = 0
        
        for word in words: 
            m = len(word)
            
            if m >= n: 
                add = True 
                
                for i in range(n):
                    if word[i] != pref[i]:
                        add = False
                        
                        break 
                        
                if add: 
                    ans += 1 
                    
        return ans 
                
        
