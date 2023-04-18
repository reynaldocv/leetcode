# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -inf 
        
        idx = 0 
        
        for (i, num) in enumerate(nums):
            if prev == num: 
                counter += 1
                
                if counter < 3: 
                    nums[idx] = num
                    
                    idx += 1 
                    
            else: 
                nums[idx] = num 
                counter = 1 
                
                idx += 1 
                
                prev = num 
                
                
        return idx
        
            
            
