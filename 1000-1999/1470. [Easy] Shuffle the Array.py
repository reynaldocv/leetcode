# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        l = len(nums)//2
        for i in range(l):
            ans.append(nums[i])
            ans.append(nums[i + l])
        return ans
        
