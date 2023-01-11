# https://leetcode.com/problems/license-key-formatting/
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ""
        
        cnt = 0 
        
        for char in s[:: -1]:
            if char != "-":
                cnt = (cnt + 1) % k 
                ans = ans + char.upper()
                
                if cnt == 0: 
                    ans += "-"
        
        if not ans: 
            return ""
        
        if ans[-1] == "-":
            ans = ans[: -1]
            
        return ans[:: -1]
                
