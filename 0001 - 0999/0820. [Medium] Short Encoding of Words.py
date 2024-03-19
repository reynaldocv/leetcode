# https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        seen = {word for word in words}
        
        for word in words: 
            for i in range(1, len(word)):
                seen.discard(word[i: ])
                
        ans = 0 
        
        for word in seen:
            ans += 1 + len(word)
            
        return ans
        
