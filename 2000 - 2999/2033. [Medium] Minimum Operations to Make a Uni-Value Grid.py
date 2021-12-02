# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        
        minNum = min(nums)
        
        for num in nums: 
            if (num - minNum) % x != 0: 
                return -1
    
        n = len(nums)
        nums.sort()
        middle = nums[n//2]
        
        ans = 0 
        for num in nums: 
            ans += abs(num - middle)//x
            
        return ans
        
 
        
