# https://leetcode.com/problems/previous-permutation-with-one-swap/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        prev = inf
        aux = []
        n = len(arr) 
        idx = n - 1
        
        while idx >= 0 and arr[idx] <= prev:
            prev = arr[idx]
            idx -= 1 
            
        if idx >= 0:                        
            idx2 = idx + 1 
            minIdx2 = (inf, idx + 1)
            while idx2 < n and arr[idx2] < arr[idx]:
                minIdx2 = min(minIdx2, (arr[idx] - arr[idx2], idx2))
                idx2 += 1
            
            idx2 = minIdx2[1]
            
            arr[idx], arr[idx2] = arr[idx2], arr[idx]
        
        return arr
