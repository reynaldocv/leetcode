# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def helper(arr, m):
            ans = [0 for _ in range(n)]
            prev = 0
            for i in range(n):
                prev += arr[i]
                if i + 1 >= m:                
                    prev -= arr[i - m] if i - m >= 0 else 0 
                    ans[i] = max(prev, ans[i - 1])
                    
            return ans

        n = len(nums)
        m, l = firstLen, secondLen
        
        left = helper(nums, m)
        right = helper(nums[::-1], m)[::-1]
        
        prev = sum(nums[:l])
        ans = prev + right[l]
        
        for (i, num) in enumerate(nums[l:]):
            prev += num - nums[i]
            val1 = left[i] if i >= 0 else 0 
            val2 = right[i + l + 1] if i + l + 1 <= n - 1 else 0
            
            ans = max(ans, prev + max(val1, val2))
    
        return ans
