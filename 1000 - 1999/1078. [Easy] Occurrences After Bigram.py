# https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(" ")
        n = len(text)
        ans = []
        for i in range(n - 2):
            if text[i] == first and text[i + 1] == second:
                ans.append(text[i + 2])
                
        return ans
        
