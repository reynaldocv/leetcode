# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic, n = {}, len(nums)
        for i in range(n):
            if nums[i] in dic and (i - dic[nums[i]]) <= k:
                    return True                
            else: 
                dic[nums[i]] = i
        
        return False
        
