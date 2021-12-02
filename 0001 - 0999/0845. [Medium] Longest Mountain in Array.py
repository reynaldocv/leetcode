# https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = [0]*n, [0]*n
        left[0],  right[-1] = 0, 0
        
        for i in range(1, n):
            left[i] = left[i - 1] + 1 if arr[i - 1] < arr[i] else 0
        
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + 1 if arr[i] > arr[i + 1] else 0
            
        ans = 0
        
        for i in range(n):
            aux = left[i] + right[i] + 1 if left[i] and right[i] else 0
            ans = max(ans, aux)
            
        return ans
        
class Solution2:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = start = 0 
        
        while start < n: 
            end = start
            
            if end + 1 < n and arr[end] < arr[end + 1]:
                while end + 1 < n and arr[end] < arr[end + 1]:
                    end += 1
                
                if end + 1 < n and arr[end] > arr[end + 1]:
                    while end + 1 < n and arr[end] > arr[end + 1]:
                        end += 1
                    
                    ans = max(ans, end - start + 1)
                    
            start = max(start + 1, end)
            
        return ans
        
