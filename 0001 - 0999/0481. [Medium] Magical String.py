# https://leetcode.com/problems/magical-string/

class Solution:
    def magicalString(self, n: int) -> int:  
        arr = [1, 2, 2]
        counter = 2
        
        while len(arr) < n:
            key = arr[counter]
            lastKey = arr[-1]
            if lastKey == 1:
                arr += [2] * key
            else:
                arr += [1] * key
            
            counter += 1
            
        return arr[:n].count(1)
        
