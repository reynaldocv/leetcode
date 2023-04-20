# https://leetcode.com/submissions/detail/522030145/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def helper(wordA, wordB):
            m, n = len(wordA), len(wordB)
            
            if m < n: 
                return False 
            
            for (i, char) in enumerate(wordB):
                if char != wordA[i]:
                    return False 
                
            return True 
        
        sentence = sentence.split(" ")
        
        for (i, word) in enumerate(sentence): 
            if helper(word, searchWord):
                return i + 1
            
        return -1
            
        
