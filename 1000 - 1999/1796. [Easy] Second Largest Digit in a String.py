# https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution:
    def secondHighest(self, s: str) -> int:
        seen = set()
        
        for char in s: 
            if char in "0123456789":
                seen.add(int(char))
                
        first = None 
        
        for num in range(9, -1, -1):
            if num in seen: 
                if first: 
                    return num

                else: 
                    first = num

        return -1
        
        
