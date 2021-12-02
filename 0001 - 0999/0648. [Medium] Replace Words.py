# https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in cur: 
                    return word[:i]
                
            return word
        
        cur = {word: True for word in dictionary}   
        
        return " ".join([replace(word) for word in sentence.split(" ")])
