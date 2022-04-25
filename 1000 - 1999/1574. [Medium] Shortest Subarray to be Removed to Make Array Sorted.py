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

class Solution2:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        left = []        
        prev = -inf
        
        for num in arr: 
            if prev <= num: 
                left.append(num)
                prev = num
            else: 
                break
                
        right = []        
        prev = inf
        
        for num in arr[::-1]:
            if prev >= num: 
                right.insert(0, num)
                prev = num
            else: 
                break
                
        ans = n - max(len(left), len(right))
        
        if ans == 0: 
            return ans 
        
        for (i, num) in enumerate(left): 
            idx = bisect_left(right, num)
            if idx == len(right):
                ans = min(ans, n - i + 1)
            else: 
                ans = min(ans, n - (len(right) - idx + 1) - i)

        return ans 
