# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr) 
        
        start = -1 
        end = n 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if arr[mid - 1] <= arr[mid]:
                start = mid 
            else: 
                end = mid 
                
        return start
            
