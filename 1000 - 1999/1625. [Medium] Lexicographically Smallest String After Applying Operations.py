# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def helper(val):
            ans = ""
            for (i, char) in enumerate(val):
                if i % 2 == 1: 
                    char = str((int(char) + a) % 10)
                
                ans += char
                
            return ans
        
        def collaborator(val):
            return val[-b:] + s[: -b]
        
        seen = set()
        stack = [s]
        while stack: 
            s = stack.pop()
            seen.add(s)
            
            newS = helper(s)
            if newS not in seen: 
                stack.append(newS)
            
            newS = collaborator(s)
            if newS not in seen: 
                stack.append(newS)
        
        return min(seen)
        
