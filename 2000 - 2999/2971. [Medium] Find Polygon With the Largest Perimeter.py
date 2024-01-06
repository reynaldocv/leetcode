# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        aSum = 0 
        
        ans = -1
        
        nums.sort() 
        
        for (i, num) in enumerate(nums):
            if aSum > num: 
                if i >= 2: 
                    ans = num + aSum
                    
            aSum += num 
            
        return ans
            
            
        
