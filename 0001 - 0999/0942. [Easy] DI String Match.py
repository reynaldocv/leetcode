# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        
        ans = []
        
        left = 0 
        right = n 
        
        for i in range(n):
            if s[i] == "I":
                ans.append(left)
                left += 1
            
            else:
                ans.append(right)
                right -= 1
            
        ans.append(right)
        
        return ans
        
            
