# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        l = len(arr)
        for i in range(l):
            for j in range(1, l + 1 - i, 2):
                ans += sum(arr[i:i + j])
        return ans
        
