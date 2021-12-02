# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}
        
        l = len(nums)
        aux = [(nums[i], i) for i in range(l)]
        aux.sort()
        for i in range(l):
            if aux[i][0] not in dict:
                dict[aux[i][0]] = i
        for i in range(l):
            nums[i] = dict[nums[i]]
        return nums
        
