# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if k > n: 
            return 0 
        
        prev = sum(arr[:k])
        ans = 1 if prev/k >= threshold else 0 
        
        for i in range(k, n):
            prev += arr[i] - arr[i - k]
            ans = ans + 1 if prev/k >= threshold else ans 
        
        return ans
            
    
