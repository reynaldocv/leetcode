# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        
        for char in address:
            if char == ".":
                ans += "[.]"
            else: 
                ans += char 
                
        return ans 
        
