# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = OrderedDict()
        for num in arr: 
            if num in seen: 
                seen[num] += 1  
            else: 
                seen[num] = 1
                
        arr = []
        for key in seen: 
            if seen[key] <= 1: 
                arr.append(key)
                
        return arr[k - 1] if k <= len(arr) else ""
           
        
            
