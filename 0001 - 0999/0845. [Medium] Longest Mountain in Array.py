# https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr) 
        
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1
            
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1
                
        ans = 0 
                
        for i in range(1, n - 1):
            if left[i] >= 1 and right[i] >= 1: 
                ans = max(ans, left[i] + right[i] + 1)
            
        return ans 
        
        

