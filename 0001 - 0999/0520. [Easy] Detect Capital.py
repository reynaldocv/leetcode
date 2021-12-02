# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lowercases = {chr(ord("a") +i) for i in range(26)}
        uppercases = {chr(ord("A") +i) for i in range(26)}
        n = len(word)
        if word[0] in lowercases:
            for i in range(1, n):
                if word[i] in uppercases:
                    return False
            return True            
        else:
            if n == 1: 
                return True
            if word[1] in lowercases: 
                for i in range(2, n):
                    if word[i] in uppercases:
                        return False
                return True
            else:
                for i in range(2, n):
                    if word[i] in lowercases:
                        return False
                return True
        
