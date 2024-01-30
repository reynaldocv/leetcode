# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def helper(aSum, idx):
            if idx == n: 
                if aSum == target: 
                    return 1 
                
                return 0 
            
            else: 
                ans = helper(aSum + nums[idx], idx + 1)
                ans += helper(aSum - nums[idx], idx + 1)
                
                return ans 
                
        n = len(nums)
        
        return helper(0, 0)
            

class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = {}
        dic[nums[0]] = 1
        dic[-nums[0]] = dic.get(-nums[0], 0) + 1
        
        for i in range(1, len(nums)):
            dic2 = {}
            for _sum in dic: 
                dic2[_sum + nums[i]] = dic2.get(_sum + nums[i], 0) + dic[_sum]
                dic2[_sum - nums[i]] = dic2.get(_sum - nums[i], 0) + dic[_sum]
                
            dic = dic2
        
        return 0 if target not in dic else dic[target]
