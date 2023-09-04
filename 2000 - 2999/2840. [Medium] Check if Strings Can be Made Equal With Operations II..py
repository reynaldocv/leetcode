# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        counter = defaultdict(lambda: 0)
        counterEven = defaultdict(lambda: 0)
        
        for (i, char1) in enumerate(s1):
            char2 = s2[i]
            
            counter[char1] += 1 
            counter[char2] -= 1 
            
            if counter[char1] == 0: 
                counter.pop(char1)
            
            if counter[char2] == 0: 
                counter.pop(char2)
            
            if i % 2 == 0:            
                counterEven[char1] += 1 
                counterEven[char2] -= 1 
                
                if counterEven[char1] == 0: 
                    counterEven.pop(char1)
            
                if counterEven[char2] == 0: 
                    counterEven.pop(char2)
                    
        return len(counter) == 0 and len(counterEven) == 0
            
                
