# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        end = bisect_left(nums, 0)
        start = end - 1 

        counter = 0

        ans = [] 

        while counter < n: 
            val1 = nums[start]**2 if start >= 0 else inf 
            val2 = nums[end]**2 if end < n else inf 

            if val1 < val2: 
                ans.append(val1)
                start -= 1 
            else:
                ans.append(val2)
                end += 1 

            counter += 1 

        return ans 
Console

