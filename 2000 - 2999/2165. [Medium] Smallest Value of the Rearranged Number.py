# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: 
            return 0 
        
        elif num > 0: 
            arr = sorted([char for char in str(num)])
            
            idx = 0 
            
            while idx >= 0 and arr[idx] == "0":
                idx += 1 
                
            first = arr.pop(idx)
            
            return int(first + "".join(arr))
            
            
            
        else: 
            num = abs(num)
            
            arr = sorted([char for char in str(num)])
            
            return -1*int("".join(arr[:: -1]))
        
