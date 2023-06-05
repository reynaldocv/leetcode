# https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        
        start = 0 
        end = n - 1
        
        arr = [char for char in s]
        
        while start < end: 
            if arr[start] != arr[end]:
                minChar = min(arr[start], arr[end])
                
                arr[start] = arr[end] = minChar
                
            start += 1 
            end -= 1 
            
        return "".join(arr)
    
