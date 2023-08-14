# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        if x == 0: 
            return 0 
        
        else: 
            ans = inf
            
            arr = nums[x: ]
            arr.sort()
            
            for (i, num) in enumerate(nums):
                idx = bisect_left(arr, num)
                
                if idx < len(arr):
                    ans = min(ans, arr[idx] - num)
                
                if idx > 0: 
                    ans = min(ans, num - arr[idx - 1])
                    
                if i + x < n: 
                    idx = bisect_left(arr, nums[i + x])
                    
                    arr.pop(idx)
                                        
                if i - x + 1 >= 0: 
                    insort(arr, nums[i - x + 1])
                    
            return ans 
