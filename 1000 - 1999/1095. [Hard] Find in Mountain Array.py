# https://leetcode.com/problems/find-in-mountain-array/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        start = 0 
        end = n 
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if mountain_arr.get(middle - 1) < mountain_arr.get(middle):
                start = middle 
                
            else: 
                end = middle 
                
        top = start
                
        start = -1 
        end = top
    
        while end - start > 1: 
            middle = (end + start)//2
            
            if mountain_arr.get(middle) < target:
                start = middle 
                
            else:
                end = middle 
                
        if mountain_arr.get(end) == target: 
            return end 
        
        start = top
        end = n
    
        while end - start > 1: 
            middle = (end + start)//2
            
            if mountain_arr.get(middle) < target:
                end = middle 
                
            else:
                start = middle 
        if mountain_arr.get(start) == target:
            return start
        
        return -1 
        
