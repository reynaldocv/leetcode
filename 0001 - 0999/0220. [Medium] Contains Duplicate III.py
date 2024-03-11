# https://leetcode.com/problems/contains-duplicate-iii/

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        arr = []
        
        i = 0 
          
        for num in nums: 
            idx = bisect_left(arr, num)
            
            if idx < len(arr):
                if arr[idx] - num <= valueDiff: 
                    return True 
                
            if 0 <= idx - 1:
                if num - arr[idx - 1] <= valueDiff: 
                    return True 
                
            if len(arr) == indexDiff: 
                idx = bisect_left(arr, nums[i])            
                arr.pop(idx)
                
                i += 1 
            
            insort(arr, num)
            
        return False 
                
        
        
