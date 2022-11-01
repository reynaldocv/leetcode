# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        
        for (i, num) in enumerate(nums):
            idx = index[i]
            
            ans.insert(idx, num)
            
        return ans 
        
