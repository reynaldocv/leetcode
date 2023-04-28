# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        
        lastA = -1
        firstB = n 
        
        for (i, char) in enumerate(s): 
            if char == "a":
                lastA = i 
                
            elif firstB == n: 
                firstB = i 
                
        return lastA + 1 == firstB
        
class Solution2:
    def checkString(self, s: str) -> bool:
        arr = [char for char in s]
        
        n = len(arr)
        
        start = 0 
        
        while start < n and arr[start] == "a":
            arr[start] = ""
            
            start += 1 
            
        end = n - 1
        
        while 0 <= end and arr[end] == "b":
            arr[end] = ""
            
            end -= 1 
            
        return "".join(arr) == ""
        
