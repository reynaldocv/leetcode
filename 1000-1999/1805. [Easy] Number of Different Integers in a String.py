# https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        n = len(word)
        numbers, nums = set([]), "1234567890"
        aux = ""
        for i in range(n):
            if word[i] in nums: 
                aux += word[i] 
            else: 
                if len(aux) > 0:
                    numbers.add(int(aux))
                aux = ""
        if len(aux) > 0:
            numbers.add(int(aux))
        
        return len(numbers)
        
        
        
        
