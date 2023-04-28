# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter = defaultdict(lambda: 0)
        
        for char in word1: 
            counter[char] += 1 
            
        for char in word2: 
            counter[char] -= 1 
            
        for key in counter: 
            if abs(counter[key]) > 3: 
                return False 
            
        return True 
        
                
        
