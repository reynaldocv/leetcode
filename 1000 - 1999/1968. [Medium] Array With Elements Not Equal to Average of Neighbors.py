https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        start = 0
        end = len(nums) - 1
        count = 1
        while end - start >= 0: 
            if count == 1: 
                ans.append(nums[end])
                end -= 1
            else:
                ans.append(nums[start])
                start += 1
            count = (count + 1) % 2
        return ans
            
            
