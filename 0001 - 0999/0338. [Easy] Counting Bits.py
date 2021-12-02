# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        if n >= 2: 
            ans = [0, 1]
        
            aux, j = 2, 0
            for i in range(2, n + 1):
                ans.append(ans[i - aux] + 1)
                j += 1
                if j == aux:
                    aux = 2*aux
                    j = 0
            
            return ans
        
