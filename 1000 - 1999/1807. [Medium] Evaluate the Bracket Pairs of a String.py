# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        replace = {}
        for (a, b) in knowledge: 
            replace["(" + a + ")"] = b
            
        key = ""
        ans = ""
        save = False
        for char in s: 
            if char not in "()":
                if key: 
                    key += char
                else: 
                    ans += char
            elif char == "(": 
                save = True
                key = char
            else: 
                key += ")"
                if key in replace: 
                    ans += replace[key]
                else:
                    ans += "?"
                save = False
                key = ""
        
        return ans
            
            
        
        
