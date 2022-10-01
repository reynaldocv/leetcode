# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {}
        
        for (i, row) in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"]):
            for char in row: 
                rows[char] = i 
                
        ans = []
        
        for word in words: 
            tmp = set()
            for char in word: 
                tmp.add(rows[char.lower()])
                
            if len(tmp) == 1: 
                ans.append(word)
                
        return ans 
