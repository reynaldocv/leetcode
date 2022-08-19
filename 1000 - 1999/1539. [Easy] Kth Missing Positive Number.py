# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def helper(value):
            idx = bisect_left(arr, value)            
            ans = value - idx
            
            if idx < n and arr[idx] == value: 
                ans -= 1 
                
            return ans 
            
        n = len(arr)
        
        start = 0 
        end = arr[-1] + k 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid) < k: 
                start = mid 
            else: 
                end = mid 
                
        return end             
