# https://leetcode.com/problems/arithmetic-slices/# 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        r = inf
        count = 1
        ans = 0
        for i in range(1, n):
            newR = nums[i] - nums[i - 1]
            if r == newR: 
                count += 1
            else: 
                if count >= 3: 
                    ans += (count - 2)*(count - 1)//2
                r = newR
                count = 2
        
        
        ans = ans + (count - 2)*(count - 1)//2 if count >= 3 else ans
        
        return ans
