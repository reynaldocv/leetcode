# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) 
        
        nums.sort()
        
        ans = set()
        
        for (i, num) in enumerate(nums):
            start = i + 1
            end = n - 1
            
            while end > start: 
                tmp = num + nums[start] + nums[end]
                if tmp == 0: 
                    ans.add((num, nums[start], nums[end]))
                    
                    start += 1 
                    end -= 1 
                    
                elif tmp < 0: 
                    start += 1 
                    
                else: 
                    end -= 1 
                    
        return ans 
        
                    
