# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        
        stack = []
        
        for word in path: 
            if word != "" and word != ".":
                if word == "..":
                    if stack: 
                        stack.pop() 
                        
                else: 
                    stack.append(word)
                    
        return "/" + "/".join(stack)
                        
                
            
        
