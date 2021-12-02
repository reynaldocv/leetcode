# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def helper(arr):
            if len(arr) == 1: 
                return arr[0] + " "*(maxWidth - len(arr[0]))
                                     
            totalLetters = sum(len(word) for word in arr)
            spaces = maxWidth - totalLetters
            quo = spaces // (len(arr) - 1)
            res = spaces % (len(arr) - 1)
            
            cnt = 0
            ans = ""
            for i in range(len(arr) - 1):
                ans += arr[i] + " "*(quo + 1) if cnt < res else arr[i] + " "*(quo)
                cnt += 1
            ans += arr[-1]
            
            return ans
        
        lines = []        
        cnt = 0 
        _words = []
        for word in words: 
            if (cnt == 0 and len(word) <= maxWidth) or (cnt > 0 and cnt + 1 + len(word) <= maxWidth):
                _words.append(word)
                cnt = len(word) if cnt == 0 else len(word) + 1 + cnt
            else: 
                lines.append(helper(_words))
                cnt = len(word)
                _words = [word]
        
        if _words: 
            aux = " ".join(_words)
            lines.append(aux + " "*(maxWidth - len(aux)))
        
        return lines
            
        
