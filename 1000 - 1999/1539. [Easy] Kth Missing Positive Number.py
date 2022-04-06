# https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def helper(value):
            start = -1         
            end = n 
            
            while end - start > 1: 
                mid = (end + start)//2 
                if arr[mid] < value: 
                    start = mid
                else: 
                    end = mid
                    
            if end == n:
                return value - end + 1
            elif arr[end] == value: 
                return value - end 
            else: 
                return value - end + 1
            
        arr.insert(0, 0)          
        n = len(arr)
        
        start = 0 
        end = 2000
        
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
