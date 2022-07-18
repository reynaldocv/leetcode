# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def helper(nums):
            return sum([int(char) for char in str(num)])
            
        ans = -1
        seen = {}
        
        nums.sort()
        
        for num in nums: 
            tmp = helper(num)
            if tmp in seen: 
                ans = max(ans, num + seen[tmp])
                
            seen[tmp] = num
            
        return ans 
