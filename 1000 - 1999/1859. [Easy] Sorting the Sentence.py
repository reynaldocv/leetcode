# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        
        s.sort(key = lambda item: item[-1: ])
        
        ans = [word[: -1] for word in s]
        
        return " ".join(ans)
        
