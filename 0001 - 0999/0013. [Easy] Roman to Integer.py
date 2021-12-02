# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        val = 0
        n = len(s)
        ans = 0
        for i in range(n - 1, -1, -1):
            if values[s[i]] >= val: 
                ans += values[s[i]]
                val = values[s[i]]
            else: 
                ans -= values[s[i]]
        return ans
            
        
        
