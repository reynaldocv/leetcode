# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        aux = ""
        n = len(s)
        for i in range(n):
            aux = aux + str(ord(s[i]) - ord("a") + 1)
        e = 0
        while e < k:
            sum_ = 0
            for i in aux: 
                sum_ += int(i)
            aux = str(sum_)
            e += 1
            
        return int(aux)
        
        
