# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr) 
        
        arr.sort() 
        
        ratio = arr[1] - arr[0]
        
        for i in range(2, n):
            if arr[i] - arr[i - 1] != ratio: 
                return False 
            
        return True 
                
        
