# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        dic[nums[0]] = 0
        
        for i in range(1, len(nums)):
            aux = target - nums[i]
            if aux in dic:
                return (dic[aux], i)
            else:
                dic[nums[i]] = i
            
        
        
