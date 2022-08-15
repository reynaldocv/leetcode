# https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = ["" for _ in range(n + 1)]
        
        stack = []
        value = 1 
        for (i, char) in enumerate(pattern + "I"):
            if char == "I":
                ans[i] = str(value)
                value += 1 
                
                while stack: 
                    ans[stack.pop()] = str(value)
                    value += 1                     
            else: 
                stack.append(i)
                
        return "".join(ans)
            
            
        
