# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:    
        def helper(arr):
            prefix = 0 
            ans = {0: 0}
            
            for (i, num) in enumerate(arr):
                prefix += num 
                
                ans[prefix] = i + 1
                
            return ans 
            
            
        n = len(nums)
        
        aSum = sum(nums)
        
        quo = (target//aSum)*n 
        
        target %= aSum 
        
        prefix = 0 
        index = {0: -1}
        
        ans = inf 
        
        for (i, num) in enumerate(nums):
            prefix += num
            
            tmp = prefix - target
            
            if tmp in index: 
                ans = min(ans, i - index[tmp])
                
            index[prefix] = i 
                
        left = helper(nums)
        right = helper(nums[:: -1])
        
        for key in left: 
            tmp = target - key 
            
            if tmp in right and left[key] + right[tmp] < n: 
                ans = min(ans, left[key] + right[tmp])
        
        return -1 if ans == inf else quo + ans 
            
