# https://leetcode.com/problems/remove-invalid-parentheses/

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def helper(s, index, leftCount, rightCount, leftRem, rightRem, expression):
            if index == n: 
                if leftRem == 0 and rightRem == 0: 
                    elem = "".join(expression)
                    ans[elem] = 1
            else: 
                if (s[index] == "("and leftRem > 0) or (s[index] == ")" and rightRem > 0):
                    newLeft = leftRem - 1 if (s[index] == '(') else leftRem 
                    newRight = rightRem - 1 if (s[index] == ')') else rightRem
                    helper(s, index + 1, leftCount, rightCount, newLeft, newRight, expression)
                
                expression.append(s[index])
                
                if s[index] != "(" and s[index] != ")":
                    helper(s, index + 1, leftCount, rightCount, leftRem, rightRem, expression)
                    
                elif s[index] == "(":
                    helper(s, index + 1, leftCount + 1, rightCount, leftRem, rightRem, expression)
                    
                elif s[index] == ")" and leftCount > rightCount: 
                    helper(s, index + 1, leftCount, rightCount + 1, leftRem, rightRem, expression)
            
                expression.pop()
        
        left = 0
        right = 0 
        n = len(s)
        
        for char in s: 
            if char == "(":
                left += 1
            elif char == ")":
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else left
                
        ans = {}
        helper(s, 0, 0, 0, left, right, [])
        
        return list(ans.keys())
