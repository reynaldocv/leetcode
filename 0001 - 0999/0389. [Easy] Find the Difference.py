# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = defaultdict(lambda: 0)
        
        for char in t: 
            counter[char] += 1 
        
        for char in s: 
            counter[char] -= 1 
            
            if counter[char] == 0: 
                counter.pop(char)
                
        return next(key for key in counter)
            
