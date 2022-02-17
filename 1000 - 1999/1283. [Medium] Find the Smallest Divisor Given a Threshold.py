# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(div):
            ans = 0 
            for num in nums: 
                ans += ceil(num/div)
                
            return ans
        
        start = 0
        end = max(nums)
        
        while end - start > 1: 
            mid = (end + start)//2
            if helper(mid) > threshold: 
                start = mid
            else: 
                end = mid
                
        return end
