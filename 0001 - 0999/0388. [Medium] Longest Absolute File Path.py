# https://leetcode.com/problems/longest-absolute-file-path/

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lvl = 0 
        file = False
        
        s = input.replace("\n", "*")
        s = s.replace("\t", "$")
        
        stack = []
        
        tmp = ""
        ans = 0
        
        for char in s + "*": 
            if char == "*":
                stack.append(tmp)
                
                if "." in tmp: 
                    ans = max(ans, len("/".join(stack)))
                    
                tmp = ""
                lvl = 0
                
            elif char == "$":
                lvl += 1 
                
            else: 
                while len(stack) > lvl: 
                    stack.pop()
                    
                tmp += char
                
        return ans 
            
        
        
        
            
        
                
