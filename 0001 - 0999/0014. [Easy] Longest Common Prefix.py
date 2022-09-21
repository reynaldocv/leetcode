# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n, m = len(strs), len(strs[0])
        
        ans = ""
        
        for i in range(m):
            letter = strs[0][i]
            
            for j in range(1, n):
                char = strs[j][i] if i < len(strs[j]) else ""

                if char != letter: 
                    return ans 
                
            ans += letter
            
        return ans
                    
                
