# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s) 
        
        ans = ""
        
        for (i, char) in enumerate(s): 
            if char == "?":
                seen = ans[i - 1] if i - 1 >= 0 else ""
                seen += s[i + 1] if i + 1 < n else ""
                
                for newChar in "abc":
                    if newChar not in seen: 
                        ans += newChar

                        break 
                        
            else: 
                ans += char

        return ans 
