# https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        
        for word in words: 
            for k in range(1, len(word)):
                good.discard(word[k:])
                
        ans = 0 
        for word in good:
            ans += 1 + len(word)
            
        return ans
