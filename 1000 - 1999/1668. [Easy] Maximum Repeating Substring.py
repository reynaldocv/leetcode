# https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        aux = ""
        while aux in sequence: 
            k += 1
            aux = word*k
            
            
        return k - 1
