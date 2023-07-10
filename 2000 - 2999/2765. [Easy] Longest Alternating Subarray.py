# https://leetcode.com/problems/longest-alternating-subarray/

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        greater = False
        
        ans = cnt = 0
        
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]: 
                if greater: 
                    cnt = 1
                    
                else: 
                    cnt += 1 
                    
                    greater = not greater
                
            elif nums[i] - 1 == nums[i + 1]:
                if greater: 
                    cnt += 1 
                    
                    greater = not greater
                    
                else: 
                    greater = False 
                    
                    cnt = 0 
                    
            else: 
                cnt = 0 
                
                greater = False 
            
            ans  = max(ans, cnt)
            
        return -1 if ans < 1 else ans + 1 
                    
                    
                
            
            
