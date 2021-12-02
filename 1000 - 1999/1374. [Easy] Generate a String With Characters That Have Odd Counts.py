# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return "a"*(1) + "b"*(n - 1)
        else:
            return "a"*n
        
