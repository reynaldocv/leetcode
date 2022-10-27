# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(lambda: 0)
        
        for num in arr: 
            counter[num] += 1 
    
        seen = set()
        
        for key in counter: 
            if counter[key] in seen: 
                return False 
            
            seen.add(counter[key])
            
        return True 
            
        
