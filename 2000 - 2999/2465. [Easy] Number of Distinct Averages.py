# https://leetcode.com/problems/number-of-distinct-averages/

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort() 
        
        seen = set()
        
        for i in range(n//2):
            seen.add((nums[i] + nums[n - 1 - i])/2)
            
        return len(seen)
        
