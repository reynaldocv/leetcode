# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        m = n//20
        arr = arr[:n - m]
        arr = arr[m:]
        return sum(arr)/len(arr)
        
        
