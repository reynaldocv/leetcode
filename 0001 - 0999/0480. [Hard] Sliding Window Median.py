# https://leetcode.com/problems/sliding-window-median/

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = []
        ans = []
        
        even = True if k % 2 == 0 else False
        
        for num in nums[:k - 1]:
            insort(window, num)
        
        for (i, num) in enumerate(nums[k - 1: ]):
            insort(window, num)
            if even: 
                ans.append((window[k//2] + window[k//2 - 1])/2)
            else: 
                ans.append(window[k//2])
            idx = bisect_left(window, nums[i])
            window.pop(idx)
            
        return ans
