# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arr = []
        
        for (ith, array) in enumerate(arrays):
            if len(array) == 1: 
                arr.append((array[0], ith))
                
            else: 
                arr.append((array[0], ith))
                arr.append((array[-1], ith))
        
        arr.sort() 
        
        if arr[0][1] != arr[-1][1]:
            return arr[-1][0] - arr[0][0]
        
        else: 
            return max(arr[-1][0] - arr[1][0], arr[-2][0] - arr[0][0])
        
                   
