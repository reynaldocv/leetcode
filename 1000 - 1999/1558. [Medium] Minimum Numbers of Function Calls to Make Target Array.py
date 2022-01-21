# https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        aSum = sum(nums)
        ans = 0
        
        while aSum != 0:
            for i in range(n):
                if nums[i] % 2 != 0:
                    ans += 1
                    aSum -= 1
                    
            if aSum != 0:
                for i in range(n):
                    nums[i] //= 2
                    aSum -= nums[i]

                ans += 1
                
        return ans
        
