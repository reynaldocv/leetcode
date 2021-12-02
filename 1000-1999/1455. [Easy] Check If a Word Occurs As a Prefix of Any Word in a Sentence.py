# https://leetcode.com/submissions/detail/522030145/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        n = len(sentence)
        ans = -1
        for i in range(n): 
            if searchWord in sentence[i]:
                if sentence[i].index(searchWord) == 0: 
                    ans = i + 1
                    break 
        return ans
    
            
        
