# https://leetcode.com/problems/three-equal-parts/

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        aSum = sum(arr)
        if aSum % 3 != 0:
            return [-1, -1]
        
        n = len(arr)
        if aSum == 0:
            return [0, n - 1]
        
        k = aSum//3
        idx = []
        cnt = 0 
        
        for (i, bit) in enumerate(arr):
            cnt += 1 if bit == 1 else 0 
            if cnt == 1 and bit == 1: 
                idx.append(i)
            if cnt % k == 0:
                cnt = 0
        
        j = 0 
        while idx[2] + j < n and arr[idx[0] + j] == arr[idx[1] + j] == arr[idx[2] + j]:
            j += 1 
            
        if idx[2] + j < n: 
            return [-1, -1]
        else: 
            return (idx[0] + j - 1, idx[1] + j)
        
        
        
