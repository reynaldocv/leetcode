# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = {}
        
        for word in words:
            aux = ""
            for character in word:
                aux += codes[ord(character)-97]
            ans[aux] = 1; 
        return len(ans)
