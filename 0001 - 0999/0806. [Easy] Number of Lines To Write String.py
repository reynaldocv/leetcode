# https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ans = 1 
        
        aSum = 0
        
        for char in s:
            width = widths[ord(char) - ord("a")]
            aSum += width
            
            if aSum > 100:
                ans += 1 
                
                aSum = width
                
        return [ans, aSum]
                
        
        
