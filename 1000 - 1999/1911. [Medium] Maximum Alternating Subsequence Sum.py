# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        arr = []
        for num in nums: 
            if not arr or arr[-1] != num: 
                arr.append(num)
                
        peaks, valleys = [], []
        
        m = len(arr)
        for i in range(m):
            left = -inf if i == 0 else arr[i - 1]
            right = -inf if i + 1 == m else arr[i + 1]
            if left < arr[i] and arr[i] > right: 
                peaks.append(arr[i])
                
            if 0 < i < m - 1:
                if arr[i - 1 ] > arr[i] and arr[i] < arr[i + 1]:
                    valleys.append(arr[i])
                    
        if len(peaks) == len(valleys):
            valleys.pop()
            
        return sum(peaks) - sum(valleys)

class Solution2:
        even = odd = 0      
        
        for num in nums:
            even = max(even, odd - num)
            odd = max(odd, even + num)
            
        return max(even, odd)
