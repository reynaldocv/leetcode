# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(lambda: 0)
        
        for char in magazine: 
            counter[char] += 1 
        
        for char in ransomNote: 
            counter[char] -= 1 
            
            if counter[char] < 0: 
                return False 
            
        return True 
        
        
