# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        maxElem = -1 
        
        for i in range(n - 1, -1, -1):
            num = arr[i]
            
            arr[i] = maxElem 
            
            maxElem = max(maxElem, num)
            
        return arr
