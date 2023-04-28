# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution:
    def digitCount(self, num: str) -> bool:
        counter = defaultdict(lambda: 0)
        
        for char in num: 
            counter[char] += 1 
            
        for (i, char) in enumerate(num):
            if counter[str(i)] != int(char): 
                return False 
        
        return True 
        
