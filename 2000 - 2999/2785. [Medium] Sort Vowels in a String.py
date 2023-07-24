# https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        
        for char in s: 
            if char in "AEIOUaeiou":
                vowels.append(char)
                
        vowels.sort() 
        
        ans = ""
        idx = 0 
        
        for char in s: 
            if char in "AEIOUaeiou":
                ans += vowels[idx]
                
                idx += 1 
                
            else: 
                ans += char 
                
        return ans
        
