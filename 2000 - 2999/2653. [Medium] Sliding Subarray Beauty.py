# https://leetcode.com/problems/sliding-subarray-beauty/

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        
        arr = []
        ans = []
        
        for (ith, num) in enumerate(nums):
            insort(arr, num)
            
            if ith > k - 1:
                idx = bisect_left(arr, nums[ith - k])
                
                arr.pop(idx)
                
            if ith >= k - 1:
                if arr[x - 1] <= 0:
                    ans.append(arr[x - 1])
                
                else:
                    ans.append(0)
            
        return ans 
