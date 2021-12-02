# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def finalWord(S):
            arr = []
            for c in S:
                if c != '#':
                    arr.append(c)
                elif len(arr) > 0:
                    arr.pop()
            return "".join(arr)
                
        return finalWord(s) == finalWord(t)
        
