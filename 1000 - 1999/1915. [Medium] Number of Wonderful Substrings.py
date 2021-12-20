# https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        n = len(word)
        mask = 0 
        
        prefix = defaultdict(lambda: 0)
        prefix[0] = 1 
        
        ans = 0 
        for char in word: 
            mask = mask ^ (1 << ord(char) - ord("a"))
            ans += prefix[mask]
            
            for i in range(10):
                tmp = mask ^ (1 << i)
                ans += prefix[tmp]
                
            prefix[mask] += 1
            
        return ans
            
        
        
