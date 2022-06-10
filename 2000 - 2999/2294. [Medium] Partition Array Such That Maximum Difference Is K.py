# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        last = nums[0] - 1
        
        ans = 0 
        
        for num in nums: 
            if last < num:
                ans += 1 
                last = num + k 
                
        return ans 
        
