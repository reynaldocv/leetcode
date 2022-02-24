# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def helper(arr, val):
            cnt = 0 
            ans = 0 
            for num in arr + [val + 1]:
                if num <= val: 
                    cnt += 1 
                else: 
                    ans += cnt*(cnt + 1)//2
                    cnt = 0 

            return ans 
        
        return helper(nums, right) - helper(nums, left - 1)

        
        
