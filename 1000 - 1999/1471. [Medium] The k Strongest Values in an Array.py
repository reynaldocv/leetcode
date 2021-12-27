# https://leetcode.com/problems/the-k-strongest-values-in-an-array/

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        median = arr[(n - 1)//2]
        
        arr.sort(reverse = True, key = lambda item: (abs(item - median), item))
        
        return arr[:k]
        
        
