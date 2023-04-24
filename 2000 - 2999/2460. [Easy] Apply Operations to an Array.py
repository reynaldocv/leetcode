# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        i = 0 
        
        nums += [inf]
        
        ans = []
        
        while i + 1 < n + 1: 
            if nums[i] == nums[i + 1]:
                if nums[i] != 0:
                    ans.append(2*nums[i])
                
                nums[i + 1] = 0
            
                i += 1 
                
            elif nums[i] != 0:
                ans.append(nums[i])
                
            i += 1 
            
        while len(ans) < n: 
            ans.append(0)
            
        return ans 
