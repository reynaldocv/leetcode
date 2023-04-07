# https://leetcode.com/problems/uncommon-words-from-two-sentences/ 

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = defaultdict(lambda: 0)
        
        word = ""
        
        for char in s1 + " " + s2 + " ":
            if char == " ":
                if word != "":
                    counter[word] += 1 
                
                word = ""
                
            else: 
                word += char 
                
        return [key for key in counter if counter[key] == 1]
                
        
