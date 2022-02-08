# https://leetcode.com/problems/global-and-local-inversions/

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        numLocal = 0
        numGlobal = 0

        n = len(nums)
        
        for (i, num) in enumerate(nums):
            if num > i:
                numGlobal += num - i
            elif num < i:
                numGlobal += i - num - 1
            
            if i < n - 1 and num > nums[i + 1]:
                numLocal += 1
        
        return numLocal == numGlobal
        
class Solution2:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        
        maxPrior = nums[0]
        for i in range(2, n):
            if nums[i] < maxPrior: 
                return False
            
            maxPrior = max(maxPrior, nums[i - 1])
        
        return True
