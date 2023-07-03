# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0 
        
        cnt = 0 
        
        for num in nums + [threshold + 1]:
            if num > threshold: 
                cnt = 0 
            
            elif cnt % 2 == 0:
                if num % 2 == 0: 
                    cnt += 1 
                
                else: 
                    cnt = 0
                    
            else:
                if num % 2 == 1: 
                    cnt += 1 
                    
                else: 
                    cnt = 1 
                    
            ans = max(ans, cnt)
            
        return ans 
