# https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dic = {}
        n = len(arr)
        idx = 0
        for i in range(n):
            if arr[i] == 0:
                dic[idx] = 0
                dic[idx + 1] = 0
                idx += 2
            else:               
                dic[idx] = arr[i]
                idx += 1
        
        for i in range(n):
            arr[i] = dic[i]
            
