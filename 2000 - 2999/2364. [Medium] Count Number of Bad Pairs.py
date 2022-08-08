# https://leetcode.com/problems/count-number-of-bad-pairs/

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        seen = defaultdict(lambda: 0)
        ans = 0 
        
        for (i, num) in enumerate(nums):
            tmp = num - i            
            ans += i - seen[tmp]        
            seen[num - i] += 1
            
        return ans 
