# https://leetcode.com/problems/repeated-string-match/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:        
        n, m = len(a), len(b)
        ans = 1
        
        sentence = a
        
        while len(sentence) < m + 2*n:
            idx =  sentence.find(b)
            if idx == -1:
                sentence += a
                ans += 1
            else: 
                return ans
                
        return -1
            
        
