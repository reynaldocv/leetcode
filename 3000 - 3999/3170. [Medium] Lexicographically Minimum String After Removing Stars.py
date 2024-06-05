# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

class Solution:
    def clearStars(self, s: str) -> str:
        chars = [char for char in s]
        
        heap = []
        
        for (ith, char) in enumerate(s):
            if char != "*":
                heappush(heap, (char, -ith))
                
            else: 
                chars[ith] = ""
                
                (_, idx) = heappop(heap)
                
                chars[-idx] = ""
                
        return "".join(chars)
        
