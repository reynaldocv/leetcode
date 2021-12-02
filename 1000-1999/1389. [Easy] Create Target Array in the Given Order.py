# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        l = len(nums)
        for i in range(l):
            ans.insert(index[i], nums[i])
        return ans
        
