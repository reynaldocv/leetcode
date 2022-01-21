# https://leetcode.com/problems/circular-permutation-in-binary-representation/

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:        
        arr = [0 for i in range(2**n)]
        arr[1] = 1
        
        for i in range(2, n + 1):
            val = 2**(i - 1)
            for j in range(val):                
                arr[val + j]  = arr[val - j - 1] + val
                 
        idx = arr.index(start)
        
        return arr[idx:] + arr[:idx]
      
