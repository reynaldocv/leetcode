# https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:        
        n, m = len(nums), len(str(nums[0]))
        
        level = defaultdict(lambda: defaultdict(lambda: 0))
        
        for num in nums: 
            for (ith, char) in enumerate(str(num)):
                level[ith][char] += 1 
                
        ans = m*n*(n - 1)//2
        
        for lvl in level: 
            for key in level[lvl]:
                ans -= level[lvl][key]*(level[lvl][key] - 1)//2
                
                
        return ans 
                
