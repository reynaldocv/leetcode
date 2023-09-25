# https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        
        ones = sum(1 for char in s if char == "1")
        
        return "1"*(ones - 1) + "0"*(n - ones) + "1"
