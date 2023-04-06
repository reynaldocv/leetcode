# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = defaultdict(lambda: 0)
        
        for char in s: 
            counter[char] += 1 
            
        seen = set() 
        
        for key in counter: 
            seen.add(counter[key])
            
        return len(seen) == 1
        
            
        
