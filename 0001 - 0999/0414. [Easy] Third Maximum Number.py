# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        ans = -inf
        pos = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] != ans: 
                pos += 1
                ans = nums[i]
                if pos == 3: 
                    break
        return nums[0] if pos != 3 else ans
        
                
