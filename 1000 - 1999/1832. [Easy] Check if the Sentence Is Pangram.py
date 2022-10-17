# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        
        for char in sentence: 
            seen.add(char)           
            
        return len(seen) == 26
        
            
        
        
