# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums) 
        
        nums.sort() 
        
        ans = []
        
        for i in range(n//3):
            left  = nums[3*i]
            right = nums[3*i + 2]
            
            if right - left <= k: 
                ans.append(nums[3*i: 3*i + 3])
                
            else: 
                return []
            
        return ans 
                
