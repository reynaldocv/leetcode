# https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        aSum = sum(nums)
        
        ans = (inf, -1)
        
        left = 0 
        
        for (i, num) in enumerate(nums): 
            left += num 
            aSum -= num 
            
            if i == n - 1:
                ans = min(ans, (abs(left//(i + 1)), i))
            else: 
                ans = min(ans, (abs(left//(i + 1) - aSum//(n - 1 - i)), i))
            
        return ans[1]
