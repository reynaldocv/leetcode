# https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        minElem = min(nums)
        nums.sort()
        ans = 0 
        
        for num in nums: 
            if num < minElem: 
                ans += minElem - num
            else: 
                minElem = num 
            
            minElem += 1 
            
        return ans
