# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

class Solution:
    def maxProduct(self, s: str) -> int:
        
        def allPossibilities(i, s1, s2):
            if i >= len(s):
                if s1 == s1[:: -1] and s2 == s2[:: -1]:
                    self.ans = max(self.ans, len(s1)*len(s2))
            else: 
                allPossibilities(i + 1, s1 + s[i], s2)
                allPossibilities(i + 1, s1, s2 + s[i])
                allPossibilities(i + 1, s1, s2)
               
        self.ans = 0
        allPossibilities(0, "", "")
        
        return self.ans
                
                
