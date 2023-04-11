# https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        stack = []
        
        for num in arr:
            if num != 0: 
                stack.append(num)
                
            else: 
                stack.append(0)
                stack.append(0)
                
        for (i, _) in enumerate(arr):
            arr[i] = stack[i]
                
