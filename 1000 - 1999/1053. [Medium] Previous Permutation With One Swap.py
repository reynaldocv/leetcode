# https://leetcode.com/problems/previous-permutation-with-one-swap/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        end = n - 2
        last = arr[-1]
        
        while end >= 0 and arr[end] <= arr[end + 1]:
            end -= 1 
            
        if end == -1:
            return arr 
        
        left = end 
        
        i = end + 1 
        
        end = (inf, i)
        
        while i < n and arr[left] > arr[i]:
            end = min(end, (arr[left] - arr[i], i))
            
            i += 1 
            
        right = end[1]
            
        arr[left], arr[right] = arr[right], arr[left]
        
        return arr
        
        
