# https://leetcode.com/problems/minimum-number-game/

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        nums.sort() 
        
        for i in range(n//2):
            nums[2*i], nums[2*i + 1] = nums[2*i + 1], nums[2*i]
            
        return nums
            
        
        
