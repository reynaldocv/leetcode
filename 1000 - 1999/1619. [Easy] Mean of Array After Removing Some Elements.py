# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        
        arr.sort()
        
        for i in range(1, n):
            arr[i] += arr[i - 1]
                
        end = n - n//20 - 1
        start = n//20 - 1
        
        return (arr[end] - arr[start])/(9*n//10)
        
        
        
