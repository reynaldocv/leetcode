# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution:
    def countValidWords(self, sentence: str) -> int:
        def helper(word):
            m = len(word)
            hyphens = 0
            for (i, char) in enumerate(word): 
                if char in "0123456789":
                    return False
                if char in ".,!" and i != m - 1:
                    return False
                if char == "-":
                    hyphens += 1
                    
            if hyphens == 0: 
                return True
            elif hyphens >= 2:
                return False
            else: 
                idx = word.index("-")
                m = m - 1 if word[-1] in ".,!" else m 
                if 0 < idx and idx < m - 1:
                    return True
                
                return False
            
        words = sentence.split(" ")
        
        ans = 0
        for word in words: 
            if word != "" and helper(word):
                ans += 1
              
        return ans
                    
