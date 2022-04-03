# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        stack, invalid = 0, 0
        
        i = 0 
    
        while i < n:
            if s[i] == "(":
                stack += 1
            else:
                if i + 1 == n or s[i + 1] != ")":
                    invalid += 1
                else:
                    i += 1

                if stack == 0:
                    invalid += 1
                else:
                    stack -= 1
            i += 1       

        return invalid + 2*stack
