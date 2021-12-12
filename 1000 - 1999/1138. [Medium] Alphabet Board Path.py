# https://leetcode.com/problems/alphabet-board-path/

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def helper(prev, cur):
            ans = ""
            if prev != cur:                 
                (x, y) = positions[prev]
                (r, s) = positions[cur]
                if prev == "z":
                    ans += "U"*abs(x - r) + "R"*abs(y - s)
                elif cur == "z":
                    ans += "L"*abs(y - s) + "D"*abs(x - r)
                else: 
                    ans += "U"*abs(x - r) if x > r else "D"*abs(x - r)
                    ans += "L"*abs(y - s) if y > s else "R"*abs(y - s)
            
            ans += "!"
            
            return ans
        
        positions = {}
        for i in range(26):
            positions[chr(ord("a") + i)] = (i // 5, i % 5)
            
        prev = "a"
        ans = ""
        for char in target:
            ans += helper(prev, char)
            prev = char
            
        return ans
            
            
            
        
        
        
