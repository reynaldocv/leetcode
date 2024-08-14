# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def helper(value):
            ans = 0 
            
            for (i, num) in enumerate(nums):
                idx = bisect_right(nums[i + 1: ], num + value)
                
                ans += idx 
                
            return ans 
        
        nums.sort() 
        
        start = -1 
        end = nums[-1] - nums[0]
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid) >= k: 
                end = mid 
                
            else: 
                start = mid
                
        return end
            
            
