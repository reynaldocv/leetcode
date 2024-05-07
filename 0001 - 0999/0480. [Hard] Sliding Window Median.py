# https://leetcode.com/problems/sliding-window-median/

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        arr = []
        
        for num in nums[: k - 1]:
            insort(arr, num)
        
        ans = []
        
        for (ith, num) in enumerate(nums[k - 1: ]):
            insort(arr, num)
            
            if k % 2 == 0: 
                ans.append((arr[k//2 - 1] + arr[k//2])/2)
                
            else: 
                ans.append(arr[k//2])
                
            idx = bisect_left(arr, nums[ith])            
            arr.pop(idx)
            
        return ans 
        
