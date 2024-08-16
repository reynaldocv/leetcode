# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(value):
            prev = 0 
            
            ans = 0 
            
            for num in nums: 
                prev += num 
                
                if prev >= value: 
                    ans += 1 
                    
                    if prev == value: 
                        prev = 0 
                        
                    else: 
                        prev = num
                        
            if prev > 0: 
                ans += 1 
                        
            return ans 
            
        start = max(nums) - 1
        end = sum(nums)
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid) > k: 
                start = mid 
            else: 
                end = mid 
                
        return end
                
