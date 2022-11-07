# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        values = [0, 1]
        counter = [0, 0]
        
        for char in s: 
            value = int(char)
            if value != values[0]:
                counter[0] += 1 
            
            if value != values[1]:
                counter[1] += 1 
                
            values[0] = 1 - values[0]
            values[1] = 1 - values[1]
                
        return min(counter)
            
