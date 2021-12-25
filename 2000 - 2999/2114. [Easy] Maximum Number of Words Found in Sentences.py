# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0 
        for sentence in sentences: 
            ans = max(ans, len(sentence.split(" ")))
            
        return ans
        
