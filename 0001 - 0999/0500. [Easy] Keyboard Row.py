# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        dic = {}
        for i in range(len(row)):
            for letter in row[i]:
                dic[letter] = i
        
        ans = []
        for word in words:
            auxword = word.lower()
            add = True
            aux = dic[auxword[0]]
            
            for i in range(1, len(word)):
                if aux != dic[auxword[i]]:
                    add = False
                    break
            if add: 
                ans.append(word)
        return ans
                
