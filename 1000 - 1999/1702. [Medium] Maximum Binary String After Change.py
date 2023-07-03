# https://leetcode.com/problems/maximum-binary-string-after-change/

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        n = len(binary)
        
        start = 0 
        
        while start < n and binary[start] == "1":
            start += 1 

        count = [0, 0]
        
        for char in binary[start: ]: 
            count[int(char)] += 1 
            
        if count[0] <= 1: 
            return binary
        
        else: 
            return "1"*start + "1"*(count[0] - 1) + "0" + "1"*count[1]
        
