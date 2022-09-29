# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:        
        n = len(arr) 
        
        end = bisect_left(arr, x)
        start = end - 1
        
        while k: 
            val1 = abs(x - arr[start]) if start >= 0 else inf 
            val2 = abs(x - arr[end]) if end < n else inf 
            
            if val1 <= val2: 
                start -= 1 
            else: 
                end += 1 
                
            k -= 1 
                
        return arr[start + 1: end]

        
        
