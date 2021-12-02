# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def change(n, values):
            ans = ""
            for i in range(len(n)):
                ans += values[n[i]]
            return int(ans)
        
        letters = "abcdefghij"
        values = {}
        for i in range(len(letters)):
            values[letters[i]]  = str(i)
            
        print(values)
        
        aux = change(firstWord, values)
        aux += change(secondWord, values)
        return  aux == change(targetWord, values) 
        
