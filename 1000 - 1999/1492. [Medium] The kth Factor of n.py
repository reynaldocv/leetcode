# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n + 1) if n % i == 0]
        
        if k - 1 < len(arr):             
            return arr[k - 1]
        
        else: 
            return -1
        
        
          
