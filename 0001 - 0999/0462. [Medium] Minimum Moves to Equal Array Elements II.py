# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums) 
        
        nums.sort() 
        
        prev = 0 
        aSum = sum(nums)
        
        ans = inf
        
        for (i, num) in enumerate(nums):
            left = i*num - prev
            right = aSum - (n - i)*num
            
            ans = min(ans, left + right)
            
            prev += num 
            aSum -=  num 
            
        return ans
        
class Solution2:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort()
        
        median = nums[n//2]
        
        ans = 0 
        
        for num in nums: 
            ans += abs(num - median)
            
        return ans

      
