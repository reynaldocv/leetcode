# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(idx, seen):
            if idx == n:
                return 0 
            
            else: 
                ans = 0    
                tmp = ""                
                
                for i in range(idx, n): 
                    tmp += s[i]
                    
                    if tmp not in seen: 
                        seen.add(tmp)
                        
                        ans = max(ans, 1 + helper(i + 1, seen))
                        
                        seen.remove(tmp)
                        
                return ans 
            
        n = len(s)
            
        return helper(0, set())
        
