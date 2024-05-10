# https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def helper(value):
            (counter, p, q) = (0, 0, 1) 
            
            j = 0 
            
            for i in range(n):
                while j < n and arr[i]/arr[j] > value: 
                    j += 1 
                    
                if j < n and p/q < arr[i]/arr[j]:
                    (p, q) = (arr[i], arr[j])
                    
                counter += n - j 
                
            return (counter, p, q)
            
        n = len(arr)
        
        start = 0
        end = 1 
        
        while end > start: 
            mid = (end + start)/2
        
            (counter, p, q) = helper(mid)
            
            if counter > k: 
                end = mid
            
            elif counter < k:             
                start = mid
                
            else:                
                return [p, q]
