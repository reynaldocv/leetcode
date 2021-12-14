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
        def helper():
            if target == mountain_arr.get(0):
                return 0 

            if target < mountain_arr.get(0):
                return -1

            start = 0 
            end = peak + 1

            while end - start > 1: 
                m = (start + end)//2
                values[m] = mountain_arr.get(m)
                if values[m] < target: 
                    start = m 
                else: 
                    end = m 
            
            return end if target == values[end] else -1
        
        def helper2():
            if target < mountain_arr.get(n - 1):
                return -1
            
            start = peak
            end = n + 1

            while end - start > 1: 
                m = (start + end)//2
                values[m] = mountain_arr.get(m)
                if values[m] > target: 
                    start = m 
                else: 
                    end = m 

            return end if values[end] == target else -1
                
        n = mountain_arr.length()
        start = 0 
        end = n
        values = {}
        while end - start > 1: 
            m = (start + end)//2
            values[m] = mountain_arr.get(m)
            values[m + 1] = mountain_arr.get(m + 1)
            
            if values[m] < values[m + 1]:
                start = m 
            else: 
                end = m
                
        peak = end
                
        if target > values[peak]:
            return -1
        
        if target == values[peak]:        
            return end
        
        idx = helper()
        
        return idx if idx != -1 else helper2()
        
        
        
        
        
                
        
            
        
        
