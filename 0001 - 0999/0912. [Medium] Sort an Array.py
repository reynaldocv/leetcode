# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def helper(nums):
            n = len(nums)
            if n <= 1: 
                return nums
            else: 
                arr1 = helper(nums[:n//2])
                arr2 = helper(nums[n//2:])
                ans = []
                
                while arr1 or arr2: 
                    elem1 = arr1[0] if arr1 else inf
                    elem2 = arr2[0] if arr2 else inf
                    
                    if elem1 < elem2: 
                        arr1.pop(0)
                        ans.append(elem1)
                    else: 
                        arr2.pop(0)
                        ans.append(elem2)
                        
                return ans
            
        return helper(nums)                        
                    
                    
