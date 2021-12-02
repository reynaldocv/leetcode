# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counterChars = {}
        for char in chars:
            counterChars[char] = counterChars.get(char, 0) + 1
        
        ans = 0
        for word in words:
            counter = {}
            success = True
            for char in word:
                counter[char] = counter.get(char, 0) + 1
            for char in counter:
                if counter[char] > counterChars.get(char, 0):
                    success = False
                    break
            if success:
                ans += len(word)
        return ans
        
