# 1574. Shortest Subarray to be Removed to Make Array Sorted

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1 
         
        if j == 0: 
            return 0 
        
        last = arr[j:] 
        m = len(last)
                
        ans = n - m
        prev = -1
        for (i, num) in enumerate(arr): 
            if prev <= num:                 
                idx = bisect_left(last, num)
                if idx == len(last):
                    ans = min(ans, n - m, n - i -  1)
                else: 
                    ans = min(ans, n - (i + 1) - (m - idx))
                prev = num
            else: 
                break
                
        return ans
