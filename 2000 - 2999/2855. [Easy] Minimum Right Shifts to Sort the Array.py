# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums) 
        
        arr = sorted(nums)
        
        ans = 0 
        
        for i in range(n):
            if nums == arr: 
                return ans 
            
            nums.insert(0, nums.pop())
            
            ans += 1 
            
        return -1 
                
