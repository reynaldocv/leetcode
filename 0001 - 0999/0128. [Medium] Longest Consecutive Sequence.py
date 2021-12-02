# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        prev = -inf
        ans = 0
        length = 0
        for i in range(n):
            if prev == nums[i]:
                continue
            elif prev + 1 == nums[i]:
                length += 1
                prev += 1
            else:
                ans = max(ans, length)
                prev = nums[i]
                length = 1
                
        ans = max(ans, length)
        
        return ans
            
            
            
        
