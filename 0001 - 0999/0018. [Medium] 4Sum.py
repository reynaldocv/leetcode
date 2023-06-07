# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums) 
        
        nums.sort() 
        
        ans = set()
        
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                k = j + 1
                l = n - 1
                
                while k < l:
                    aSum = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if aSum == target: 
                        ans.add((nums[i], nums[j], nums[k], nums[l]))  
                        
                        k += 1 
                        l -= 1 

                    elif aSum < target: 
                        k += 1 
                        
                    else: 
                        l -= 1 
                        
        return ans 
        
