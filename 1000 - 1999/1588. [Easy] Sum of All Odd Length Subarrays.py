# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        
        ans = 0 
        
        for (i, num) in enumerate(arr):
            left = i 
            right = n - i - 1
            
            ans += num*(left//2 + 1)*(right//2 + 1)
            ans += num*((left + 1)//2)*((right + 1)//2)
            
        return ans 
        
class Solution2:
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
        
