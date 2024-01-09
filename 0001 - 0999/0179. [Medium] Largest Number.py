# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums) 
        
        nums = [str(num) for num in nums]
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] <= nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    
        if nums[0] == "0":
            return "0"
        
        else: 
            return "".join(nums)
        
class Solution2:
    def largestNumber(self, nums: List[int]) -> str:        
        class compare(str):
            def __lt__(x, y):
                return x + y > y + x
    
        n = len(nums)
        
        nums = [str(nums[i]) for i in range(n)]
        
        nums.sort(key = compare)
        
        if nums[0] == "0":
            return "0"
        
        else: 
            return "".join(nums)
