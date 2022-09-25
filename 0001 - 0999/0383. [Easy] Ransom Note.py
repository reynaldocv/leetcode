# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(lambda: 0) 
        
        for char in magazine: 
            counter[char] += 1 
            
        for char in ransomNote: 
            if counter[char] > 0: 
                counter[char] -= 1 
            else: 
                return False 
            
        return True 
        
