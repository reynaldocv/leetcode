# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        l = len(arr)
        if l == 2:
            return True
        arr.sort()
        aux = arr[0] - arr[1]
        for i in range(1, l - 1):
            if aux != arr[i] - arr[i + 1]:
                return False
        return True
            
        
        
