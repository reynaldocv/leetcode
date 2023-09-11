# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution:
    def minimizeResult(self, expression: str) -> str:
        n = len(expression)
        
        ans = (inf, "")
        
        idx = expression.index("+")
        
        for i in range(0, idx):
            for j in range(idx + 2, n + 1):
                left = expression[: i]
                center = expression[i: j]                
                right = expression[j: ]
                
                leftVal = int(left) if left else 1 
                rightVal = int(right) if right else 1 
                
                ans = min(ans, (leftVal*eval(center)*rightVal, left + "(" + center + ")" + right))
                
        return ans[1]
                
