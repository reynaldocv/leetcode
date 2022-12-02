# https://leetcode.com/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        numbers = []
        
        for char in s: 
            if char.isdigit(): 
                numbers.append(char)
            else: 
                letters.append(char)
        
        m, n = len(letters), len(numbers)
        
        if abs(m - n) > 1: 
            return ""
        
        l = min(m, n)
        
        ans = ""
        
        for i in range(l):
            ans += letters[i] + numbers[i]
            
        if m == n: 
            return ans 
        
        elif m > n: 
            return ans + letters[-1]
        
        else: 
            return numbers[-1] + ans
            
