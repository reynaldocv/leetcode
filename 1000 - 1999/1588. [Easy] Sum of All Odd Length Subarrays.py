# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0]
        for num in arr: 
            prefix.append(prefix[-1] + num)
        
        ans = prefix[-1]
        
        for i in range(n):
            for j in range(i + 2, n, 2):
                ans += prefix[j + 1] - prefix[i]
                
        return ans
        
