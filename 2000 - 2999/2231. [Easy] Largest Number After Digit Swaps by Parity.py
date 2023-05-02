# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution:
    def largestInteger(self, num: int) -> int:    
        arr = [char for char in str(num)]
        
        even = []
        odd = []
        
        for char in arr: 
            if char in "02468":
                even.append(char)
                
            else: 
                odd.append(char)
                
        even.sort()
        odd.sort() 
        
        for (i, num) in enumerate(arr):
            if num in "02468":
                arr[i] = str(even.pop())
                
            else: 
                arr[i] = str(odd.pop())
                
        return int("".join(arr))
                
