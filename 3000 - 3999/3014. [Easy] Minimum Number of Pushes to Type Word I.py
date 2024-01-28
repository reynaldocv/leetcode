# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = defaultdict(lambda: 0)
        
        for char in word: 
            counter[char] += 1 
            
        chars = [key for key in counter]
        
        chars.sort(key = lambda item: -counter[item])
        
        ans = 0 
        
        for (i, char) in enumerate(chars): 
            times = i//8 + 1
            
            ans += times*counter[char]
            
        return ans     
        
        
        
        
