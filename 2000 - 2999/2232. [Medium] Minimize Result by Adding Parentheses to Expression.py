# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution:
    def minimizeResult(self, expression: str) -> str:
        def helper(string):
            ans = 0 
            num = ""
            for char in string + "+": 
                if char == "+":
                    ans += int(num) 
                    num = ""
                else: 
                    num += char
                    
            return ans
               
        n = len(expression)
        
        idx = next(i for (i, char) in enumerate(expression) if char == "+")
        
        ans = (helper(expression), "(" + expression + ")")
        
        for i in range(idx ):
            for j in range(idx + 1, n):
                left = 1 if i == 0 else int(expression[: i])
                right = 1 if j == n - 1 else int(expression[j + 1:])
                value = helper(expression[i: j + 1])
                newExp = expression[: i] + "(" + expression[i: j + 1] + ")" + expression[j + 1:]
                ans = min(ans, (left*value*right, newExp ))
                
        return ans[1]
                
