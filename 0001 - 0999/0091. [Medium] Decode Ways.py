# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        dic = {str(i):True for i in range(1, 27)}
        n = len(s)
        arr = [0 for i in range(n)]
        if s[0] == "0": return 0 
        if n == 1: return 1
        arr[0] = 1
        arr[1] = 1 if s[1] in dic else 0
        arr[1] += 1 if s[0] +  s[1] in dic else 0 
        
        for i in range(2, n):
            if s[i] in dic: 
                arr[i] += arr[i - 1]
            if s[i - 1] + s[i] in dic: 
                arr[i] += arr[i - 2]
       
        return arr[n - 1]
        
