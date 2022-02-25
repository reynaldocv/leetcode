# https://leetcode.com/problems/number-of-atoms/

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [defaultdict(lambda: 0)]
        
        i = 0 
        while i < n: 
            if formula[i] == "(":
                stack.append(defaultdict(lambda: 0))
                i += 1 
                
            elif formula[i] == ")":
                top = stack.pop()
                i += 1 
                start = i 
                while i < n and formula[i].isdigit():
                    i += 1 
                
                multiplicity = int(formula[start: i] or 1)
                for (name, v) in top.items(): 
                    stack[-1][name] += v*multiplicity
                    
            else: 
                start = i 
                i += 1 
                while i < n and formula[i].islower():
                    i += 1
                    
                name = formula[start: i]
                start = i 
                
                while i < n and formula[i].isdigit():
                    i += 1 
                    
                multiplicity = int(formula[start: i] or 1)
                
                stack[-1][name] += multiplicity
        
        ans = ""
        
        for key in sorted(stack[-1]):
            if stack[-1][key] > 1: 
                ans += key + str(stack[-1][key])
            else: 
                ans += key
        
        return ans
