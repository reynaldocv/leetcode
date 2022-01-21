# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def helper(val):
            idx = bisect_right(arr, val)
            ans = 0 if idx == 0 else aSum[idx - 1]
            return ans + (n - idx)*val
        
        n = len(arr)
        arr.sort()
        
        aSum = [num for num in arr]
        for i in range(1, n):
            aSum[i] += aSum[i - 1]
            
        end = arr[-1] + 1
        start = 0 
        
        while end - start > 1: 
            m = (end + start)//2
            if helper(m) <= target: 
                start = m
            else: 
                end = m 
                
        if abs(target - helper(start)) <= abs(target - helper(end)):
            return start
        else: 
            return end
