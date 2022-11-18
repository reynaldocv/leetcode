# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = defaultdict(lambda: 0)
        n = 0 
        
        for word in words: 
            n += 1 
            for char in word: 
                counter[char] += 1 
                
        for key in counter: 
            if counter[key] % n != 0: 
                return False 
        
        return True 
        
