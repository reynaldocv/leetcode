# https://leetcode.com/problems/construct-k-palindrome-strings/

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = {}
        for char in s: 
            counter[char] = counter.get(char, 0) + 1
        
        countOdd = 0
        for key in counter: 
            if counter[key] % 2 == 1:
                countOdd += 1
            
        return countOdd <= k and len(s)>= k
            
        
