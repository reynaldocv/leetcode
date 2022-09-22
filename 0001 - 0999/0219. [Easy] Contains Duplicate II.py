# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index = {}
        
        for (i, num) in enumerate(nums): 
            if num not in index: 
                index[num] = i 
                
            elif (i - index[num]) <= k:
                return True 
            
            index[num] = i 
            
        return False 
        
