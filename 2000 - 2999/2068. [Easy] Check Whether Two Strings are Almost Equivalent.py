# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = defaultdict(lambda: 0)
        counter2 = defaultdict(lambda: 0)
        keys = {}
        
        for char in word1: 
            keys[char] = True
            counter1[char] += 1
            
        for char in word2: 
            keys[char] = True
            counter2[char] += 1
            
        for key in keys: 
            if abs(counter1[key] - counter2[key]) > 3: 
                return False
            
        return True
                
        
