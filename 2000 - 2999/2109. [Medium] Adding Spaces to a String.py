# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n, m = len(s), len(spaces)
        
        j = 0 
        
        ans = ""
        
        for i in range(n):
            if j < m and spaces[j] == i: 
                ans += " "
                
                j += 1 
                
            ans += s[i]
            
        return ans 
        
