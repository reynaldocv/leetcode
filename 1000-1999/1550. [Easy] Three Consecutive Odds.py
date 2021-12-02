# https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        l = len(arr)
        for i in range(l):
            if arr[i] % 2 == 0:
                counter = 0
            else:
                counter += 1
            if counter == 3:
                return True
        return False
        
