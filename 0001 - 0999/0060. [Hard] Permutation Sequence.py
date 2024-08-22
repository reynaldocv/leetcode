# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def helper(total, ith):
            if total == 1: 
                return str(arr.pop()) 
            
            else: 
                m = len(arr)
                
                div = total//m
                
                idx = ith//div
                
                return str(arr.pop(idx)) + helper(total//m, ith % div)
                           
        arr = [i + 1 for i in range(n)]
        
        total = 1
        
        for num in range(2, n + 1):
            total *= num 
            
        return helper(total, k - 1)
