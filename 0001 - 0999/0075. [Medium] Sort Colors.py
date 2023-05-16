# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        i = 0     
        
        for num in [0, 1, 2]:
            while counter[num] > 0: 
                nums[i] = num
                
                counter[num] -= 1 
                i += 1 
                
        
        
            
