# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        seen = set()
        
        for word in words: 
            tmp = ""
            
            for char in word: 
                idx = ord(char) - ord("a")
                
                tmp += morse[idx]
                
            seen.add(tmp)
            
        return len(seen)
                
