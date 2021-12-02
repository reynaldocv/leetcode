# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def helper(expression):
            if expression.isdigit():
                return [int(expression)]
            
            ans = []
            for i in range(len(expression)):
                if expression[i] in "+-*":
                    left = helper(expression[:i])
                    right = helper(expression[i + 1:])
                    for l in left: 
                        for r in right: 
                            if expression[i] == "-":
                                ans.append(l - r)
                            elif expression[i] == "+":
                                ans.append(l + r)
                            else:
                                ans.append(l * r)
                                
            return ans
        
        return helper(expression)
        
