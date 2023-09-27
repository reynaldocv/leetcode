# https://leetcode.com/problems/decoded-string-at-index/

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0 
        
        for char in s: 
            if char.isdigit():
                size *= int(char)
                
            else: 
                size += 1 
                
        for char in s[::-1]:
            k %= size
            
            if k == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                size /= int(char)
                
            else: 
                size -= 1 
        
