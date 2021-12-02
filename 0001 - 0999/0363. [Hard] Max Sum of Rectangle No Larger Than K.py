# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = -inf
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n):
            preSum = [0]*m
            
            for ii in range(i, n):
                for j in range(m):
                    preSum[j] += matrix[ii][j]
                    
                arr = [0, inf]
                curSum = 0
                for pSum in preSum: 
                    curSum += pSum
                    idx = bisect_left(arr, curSum - k)
                    ans = max(ans, curSum - arr[idx])
                    if ans == k: 
                        return k
                    insort(arr, curSum)
        
        return ans
                
