# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s) 
        
        arr = [char for char in s]
        
        for i in range(n - 1):
            if int(arr[i]) % 2 == int(arr[i + 1]) % 2: 
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                    break 
                
        return "".join(arr)
       
