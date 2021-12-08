# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.append(0)
        
        stack = [-1]
        ans = 0
        
        for (i, num) in enumerate(arr):
            while len(stack) > 1 and arr[stack[-1]] > num: 
                last = stack.pop()
                ans += (last - stack[-1])*(i - last)*arr[last] % MOD
                
            stack.append(i)
            
        return ans % MOD
        
