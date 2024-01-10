# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def helper(sentence):
            if sentence.isdigit(): 
                return [int(sentence)]
            
            else: 
                ans = []
                
                for (i, char) in enumerate(sentence):
                    if char in "+-*":
                        left = helper(sentence[: i])
                        right = helper(sentence[i + 1: ])
                        
                        for l in left: 
                            for r in right: 
                                if char == "+":
                                    ans.append(l + r)

                                elif char == "-":
                                    ans.append(l - r)
                                    
                                else: 
                                    ans.append(l*r)
                                    
                return ans 
            
        return helper(expression)
