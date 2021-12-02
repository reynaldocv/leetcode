# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        minstr = strs[0]
        for a in strs: 
            if len(a) <= len(minstr): 
                minstr = a
        
        for i in range(len(minstr)):
            go = True
            for j in range(len(strs)):
                if strs[j][i] != minstr[i]:
                    go = False
                    break
            if go: 
                ans += minstr[i]
            else: 
                break
        return ans
                    
                
