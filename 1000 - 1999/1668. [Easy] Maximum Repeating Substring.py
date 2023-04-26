# https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        start = 0
        end = len(sequence) + 1
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if word*middle in sequence: 
                start = middle 
                
            else: 
                end = middle 
                
        return start
