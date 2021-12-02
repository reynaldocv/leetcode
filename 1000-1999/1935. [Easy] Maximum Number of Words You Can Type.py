# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        dic = {i: True for i in brokenLetters}
        textSplit = text.split(" ")
        
        ans = 0
        for word in textSplit:
            go = True        
            for w in word: 
                if w in dic: 
                    go = False
                    break
            if go:
                ans += 1
        return ans
        
