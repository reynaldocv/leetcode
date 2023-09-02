# https://leetcode.com/problems/extra-characters-in-a-string/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache 
        def helper(i):
            if i == n: 
                return 0
            
            else: 
                ans = 1 + helper(i + 1)
                
                tmp = ""
                
                for j in range(i, n): 
                    tmp += s[j]
                    
                    if tmp in dictionary:
                        ans = min(ans, helper(j + 1))
                    
                return ans
        
        dictionary = {word for word in dictionary}
        
        n = len(s)
        
        return helper(0)
        
