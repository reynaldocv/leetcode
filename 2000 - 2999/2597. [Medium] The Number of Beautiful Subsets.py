# https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def helper(arr, idx):
            nonlocal ans 
            
            if arr:                 
                ans += 1                 

            for i in range(idx, n):                
                value = nums[i]
                
                idx = bisect_left(arr, value - k)
                
                if idx == len(arr) or (idx < len(arr) and (arr[idx] != value - k)): 
                    arr.append(value)

                    helper(arr, i + 1)

                    arr.pop()
                
        n = len(nums)
        
        nums.sort()
        
        ans = 0 
        
        for i in range(n):        
            helper([nums[i]], i + 1)
        
        return ans 
                
