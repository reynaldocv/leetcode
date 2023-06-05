# https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        
        nums.sort() 
        
        ans = (inf, inf)
        
        for (i, num) in enumerate(nums):
            start = i + 1
            end = n - 1
            
            while start < end: 
                aSum = num + nums[start] + nums[end]                
                ans = min(ans, (abs(target - aSum), aSum))
            
                if aSum <= target: 
                    start += 1 
                    
                else: 
                    end -= 1 
                    
        return ans[1]
                    
