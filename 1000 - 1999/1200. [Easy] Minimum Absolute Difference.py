# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = inf 
        
        n = len(arr)
        
        arr.sort() 
            
        ans = []
        
        for i in range(n - 1):
            if arr[i + 1] - arr[i] < minDiff:                 
                ans = [[arr[i], arr[i + 1]]]
                minDiff = min(minDiff, arr[i + 1] - arr[i])       
            
            elif arr[i + 1] - arr[i] == minDiff:
                ans.append([arr[i], arr[i + 1]])
                
        return ans 
