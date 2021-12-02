# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prevSum = 0
        postSum = sum(nums) - nums[0]
        
        ans = [0 for _ in range(n)]
        for i in range(n):                                    
            ans[i] = (postSum - (n - 1 - i)*nums[i]) + (i*nums[i] - prevSum)
            prevSum += nums[i]
            if i < n-1:
                postSum -= nums[i + 1]
                
        return ans
                
            
            
        
