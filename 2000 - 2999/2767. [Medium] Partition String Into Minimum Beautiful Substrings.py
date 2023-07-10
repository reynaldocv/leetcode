# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        @cache
        def helper(word):
            if word == "": 
                return 0 
            
            else: 
                ans = inf 
                
                tmp = ""
                
                for (i, char) in enumerate(word):
                    tmp += char 
                    
                    if tmp in seen: 
                        ans = min(ans, 1 + helper(word[i + 1: ]))
                        
                return ans 
            
        seen = {str(bin(5**i))[2: ] for i in range(8)}
        
        ans = helper(s)
        
        return -1 if ans == inf else ans 
        
        
