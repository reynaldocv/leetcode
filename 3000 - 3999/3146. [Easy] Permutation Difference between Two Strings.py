# https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index = {}
        
        for (i, char) in enumerate(s):
            index[char] = i 
            
        ans = 0 
        
        for (i, char) in enumerate(t):
            ans += abs(index[char] - i)
            
            
        return ans 
        
