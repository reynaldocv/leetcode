# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        ans = 0 
        tmp = 0 
        
        for char in s[:: -1]:
            if values[char] < tmp: 
                ans -= values[char]
                
            else: 
                ans += values[char]
                tmp = values[char]
                
        return ans 
            
        
        
