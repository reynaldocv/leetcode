# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        aux = arr.copy()
        aux.sort()
        dic = {}
        
        j = 1
        for i in range(n):
            if aux[i] not in dic: 
                dic[aux[i]] = j
                j += 1
                
        for i in range(n):
            arr[i] = dic[arr[i]]
        
        return arr
        
