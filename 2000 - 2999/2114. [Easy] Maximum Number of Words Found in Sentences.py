# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0 
        
        for sentence in sentences: 
            cnt = 1 
            for char in sentence:
                if char == " ":
                    cnt += 1 
                    
            ans = max(ans, cnt)
            
        return ans
                    
