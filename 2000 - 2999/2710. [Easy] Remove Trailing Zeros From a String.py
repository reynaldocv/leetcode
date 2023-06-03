# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = len(num)
        
        end = n - 1
        
        while end >= 0 and num[end] == "0": 
            end -= 1 
            
        return num[: end + 1]
        
        
