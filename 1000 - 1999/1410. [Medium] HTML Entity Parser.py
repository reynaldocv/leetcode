# https://leetcode.com/problems/html-entity-parser/https://leetcode.com/problems/html-entity-parser/

class Solution:
    def entityParser(self, text: str) -> str:
        ans = ""
        code = "" 
        
        seen = {}
        seen["&quot;"] = '"'
        seen["&apos;"] = "'"
        seen["&amp;"] = "&"
        seen["&gt;"] = ">"
        seen["&lt;"] = "<"
        seen["&frasl;"] = "/"
        
        for char in text: 
            if code: 
                if char != "&":                    
                    code += char
                    if code in seen: 
                        ans += seen[code]
                        code = ""
                else: 
                    ans += code
                    code = "&"
            else: 
                if char == "&":
                    code = "&"
                else: 
                    ans += char
                    
        return ans + code if code else ans
                
                
