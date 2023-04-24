# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = defaultdict(lambda: 0)
        
        for char in word: 
            counter[char] += 1
            
        for char in word: 
            counter[char] -= 1 
            
            if counter[char] == 0: 
                counter.pop(char)
                
            seen = set([counter[key] for key in counter])
            
            if len(seen) == 1: 
                return True 
            
            counter[char] += 1 
            
        return False
