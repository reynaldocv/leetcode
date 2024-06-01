# https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sort = sorted(arr)
        
        ans = []
        
        n = len(arr)
        
        while sort: 
            elem = sort.pop()
        
            idx = arr.index(elem)
            
            arr[: idx + 1] = arr[:idx + 1][::-1]
            arr[: n] = arr[: n][::-1] 
            
            ans.extend([idx + 1, n])        
            
            n -= 1
            
        return ans
        
        
        
        
        
