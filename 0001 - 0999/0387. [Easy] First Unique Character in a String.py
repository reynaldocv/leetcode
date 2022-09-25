# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(lambda: 0)
        
        for (i, char) in enumerate(s):
            counter[char] += 1 
        
        for (i, char) in enumerate(s):
            if counter[char] == 1: 
                return i 
            
        return -1 
            
        
        
        
