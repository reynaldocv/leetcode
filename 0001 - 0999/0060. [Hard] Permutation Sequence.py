# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        elems = [str(i) for i in range(1, n + 1)]
        
        factorial = 1
        for i in range(2, n): 
            factorial *= i
            
        ans = ""
        m = n 
        
        while len(ans) < n:
            
            quo = k // factorial
            k = k % factorial
            if k == 0: 
                quo -= 1
            elem = elems.pop(quo)
            ans += elem
            m -= 1
            if m != 0:
                factorial //= m
           
        return ans
