# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        aux = s.split(" ")
        ans = ""
        if len(aux) <= k:
            return s
        
        for i in range(k):
            ans += aux[i] + " "
        
        return ans[:len(ans) - 1]
        
