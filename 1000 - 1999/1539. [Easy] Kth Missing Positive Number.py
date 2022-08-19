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

class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k <= arr[n - 1] - n:
            dic = {}
            for i in arr: 
                dic[i] = True
            idx = 0
            for i in range(1, arr[n - 1]):
                if i not in dic:  
                    idx += 1
                if idx == k:
                    return i
        else:
            aux = arr[n - 1] - n
            k -= aux
            return arr[n - 1] + k
