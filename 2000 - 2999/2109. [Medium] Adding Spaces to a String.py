# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        seen = {num: True for num in spaces}
        ans = ""
        for (i, char) in enumerate(s):
            if i in seen: 
                ans += " " + char
            else: 
                ans += char
                
        return ans
        
