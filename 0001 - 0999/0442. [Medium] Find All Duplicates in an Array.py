# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums: 
            n = abs(num)
            if nums[n - 1] < 0:
                ans.append(n)
            else: 
                nums[n - 1] *= -1
        
        return ans
        
