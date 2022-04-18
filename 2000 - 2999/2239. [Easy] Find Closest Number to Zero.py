# https://leetcode.com/problems/find-closest-number-to-zero/

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = (inf, inf)
        
        for num in nums: 
            ans = min(ans, (abs(num), -num))
                      
        return -ans[1]
        
