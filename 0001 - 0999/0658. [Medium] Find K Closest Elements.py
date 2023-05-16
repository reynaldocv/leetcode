# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr) 
        
        idx = bisect_left(arr, x)
        
        start = idx  - 1
        end = idx 
        
        for _ in range(k):
            left = abs(arr[start] - x) if start >= 0 else inf 
            right = abs(arr[end] - x) if end < n else inf 
            
            if left  <= right: 
                start -= 1 
                
            else: 
                end += 1 
            
        return arr[start + 1: end] 
                
        
        
        
