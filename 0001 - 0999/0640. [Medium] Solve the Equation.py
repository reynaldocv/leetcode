# https://leetcode.com/problems/solve-the-equation/

class Solution:
    def solveEquation(self, equation: str) -> str:
        def helper(sentence):
            ans = [0, 0]
            sign = 1
            num = ""
            for char in sentence + "+": 
                if char in "+-":
                    if num != "": 
                        ans[1] += sign*int(num)
                        
                    sign = 1 if char == "+" else -1
                    num = ""
                    
                elif char.isdigit():
                    num += char
                    
                elif char == "x":
                    ans[0] += sign*int(num) if num != "" else sign
                    sign = 1
                    num = ""
                    
            return ans
            
        sentences = equation.split("=")
        arr1 = helper(sentences[0])
        arr2 = helper(sentences[1])
        
        ans = (arr1[0] - arr2[0], arr1[1] - arr2[1])
        
        if ans[0] == 0:
            if ans[1] == 0:
                return "Infinite solutions"
            else: 
                return "No solution"            
        else: 
            return "x=" + str(-ans[1]//ans[0])
            
            
        
        
