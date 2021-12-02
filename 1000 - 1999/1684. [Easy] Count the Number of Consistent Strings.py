# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dic = {}
        for i in allowed: 
            dic[i] = True
        ans = 0
        
        
        for word in words:
            aux = True
            for w in word:
                if not dic.get(w, False):
                    aux = False
                    break
            if aux:
                ans += 1 
        return ans
        
