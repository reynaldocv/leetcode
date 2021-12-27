# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        seen = defaultdict(lambda: 0)
        
        words.sort(key = lambda item: len(item))
        ans = 0
        
        for word in words:            
            val = 0 
            for i in range(len(word)):
                aux = word[:i] + word[i + 1:]
                val = max(val, seen[aux] + 1)
            
            seen[word] = val
            ans = max(ans, seen[word])
            
        return ans
                
            
                
