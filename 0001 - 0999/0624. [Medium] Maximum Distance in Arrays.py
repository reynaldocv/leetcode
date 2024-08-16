# https://leetcode.com/problems/maximum-distance-in-arrays/

# Time complexity : O(n)
# Space complexity: O(1)
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arr = []
        
        maxElem = arrays[0][-1]
        minElem = arrays[0][0]
        
        ans = -inf 

        for array in arrays[1: ]:
            
            maxNum = array[-1]
            minNum = array[0]
            
            ans = max(ans, abs(maxNum - minElem))
            ans = max(ans, abs(maxElem - minNum))
            
            maxElem = max(maxElem, maxNum)
            minElem = min(minElem, minNum)
            
        return and     
        
# Time complexity : O(n lg n)
# Space complexity: O(n)
class Solution2:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arr = []
        
        for (ith, array) in enumerate(arrays):
            if len(array) == 1: 
                arr.append((array[0], ith))
                
            else: 
                arr.append((array[0], ith))
                arr.append((array[-1], ith))
        
        arr.sort() 
        
        if arr[0][1] != arr[-1][1]:
            return arr[-1][0] - arr[0][0]
        
        else: 
            return max(arr[-1][0] - arr[1][0], arr[-2][0] - arr[0][0])
        
                   
