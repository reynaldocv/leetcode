# https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def helper(word):
            tmp = ""
            
            for char in word: 
                tmp += char 
                
                if tmp in seen: 
                    return tmp 
                
            return word
        
        seen = {word for word in dictionary}
        
        words = sentence.split(" ")
        
        ans = []
        
        for word in words: 
            ans.append(helper(word))
            
        return " ".join(ans)
