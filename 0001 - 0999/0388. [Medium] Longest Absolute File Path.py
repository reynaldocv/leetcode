# https://leetcode.com/problems/longest-absolute-file-path/

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        arr = input.split("\n")
        stack = []        
        ans = 0
        for val in arr: 
            while stack and stack[-1].count("\t") >= val.count("\t"):
                    stack.pop()                
            if "." in val: 
                aux = "/".join(stack + [val])
                aux = aux.replace("\t","")
                
                ans = max(ans, len(aux))
                
            else: 
                stack.append(val)
        
        return ans
            
        
                
