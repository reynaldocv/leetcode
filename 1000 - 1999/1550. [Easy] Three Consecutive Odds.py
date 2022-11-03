# https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr) 
        
        counter = 0
        
        for i in range(n):
            if arr[i] % 2 == 0:
                counter = 0
        
            else:
                counter += 1
            
            if counter == 3:
                return True
        
        return False
