# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        replace = defaultdict(lambda: "?")
        
        for (a, b) in knowledge: 
            replace[a] = b 
        
        stack = [""]
        
        for char in s: 
            if char == "(":
                stack.append("")
                
            elif char == ")":
                word = stack.pop()
                
                stack.append(replace[word]) 
                
                stack.append("")
                
            else: 
                stack[-1] += char 
        
        return "".join(stack)
        
            
        
        
