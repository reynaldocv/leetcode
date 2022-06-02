# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(lambda: 0)
        
        nums.sort()
        
        ans = 0 
        
        for num in nums: 
            seen[num] = 1 + seen[num - 1]
            ans = max(ans, seen[num])

        return ans 
            
