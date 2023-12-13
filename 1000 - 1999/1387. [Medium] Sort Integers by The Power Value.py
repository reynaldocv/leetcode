# https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def helper(num):
            if num in power: 
                return power[num]
            
            elif num % 2 == 0: 
                return 1 + helper(num// 2)
            
            else: 
                return 1 + helper(3*num + 1)
        
        power = {1: 1}
        
        for i in range(2, 1001):
            power[i] = helper(i)
            
        arr = [i for i in range(lo, hi + 1)]
        
        arr.sort(key = lambda item: power[item])
        
        return arr[k - 1]
            
        
        
        
        
        
