# https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        seen = defaultdict(lambda: 0)
        
        for (start, end, direction) in shifts: 
            if direction == 1: 
                seen[start] += 1 
                seen[end + 1] -= 1
            else: 
                seen[start] -= 1 
                seen[end + 1] += 1 
        
        index = {chr(ord("a") + i): i for i in range(26)}
        chars = {i: chr(ord("a") + i) for i in range(26)}
        
        tmp = 0 
        ans = ""
        
        for (i, char) in enumerate(s):            
            tmp += seen[i]
            idx = index[char]
            
            ans += chars[((idx + tmp) % 26)]
            
        return ans 
            
            
