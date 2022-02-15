# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: 
            return arr[0]
                
        left = [num for num in arr]        
        for i in range(1, n):            
            left[i] = max(left[i], left[i - 1] + left[i])
            
        right = [num for num in arr]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i], right[i + 1] + right[i])
            
        ans = -inf
        for i in range(n):
            l = -inf if i == 0 else left[i - 1]
            r = -inf if i == n - 1 else right[i + 1]
            ans = max(ans, l + r, l, r, l + r + arr[i])
            
        return ans
