# https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def helper(sentence):
            counter = [0]*5
            for char in sentence: 
                if char not in "aeiou":
                    return False
                else: 
                    counter[index[char]] = 1
            
            return sum(counter) == 5
                
        n = len(word)
        index = {char: i for (i, char) in enumerate("aeiou")}
        
        ans = 0
        for i in range(n - 5 + 1):
            for j in range(i + 5, n + 1):
                if helper(word[i: j]):
                    ans += 1
                
        return ans 
    
