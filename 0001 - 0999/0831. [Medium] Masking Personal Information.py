# https://leetcode.com/problems/masking-personal-information/

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s: 
            arr = (s.lower()).split("@")
            arr[0] = arr[0][0] + "*****" + arr[0][len(arr[0]) - 1]
            return "@".join(arr)
            
        else: 
            onlyNumbers = ""
            for letter in s: 
                if letter in "0123456789":                    
                    onlyNumbers += letter
            n = len(onlyNumbers) 
            if n == 10:
                ans = "***-***-" + onlyNumbers[6:]
            elif n == 11: 
                ans = "+*-***-***-" + onlyNumbers[7:]
            elif n == 12: 
                ans = "+**-***-***-" + onlyNumbers[8:]
            else: 
                ans = "+***-***-***-" + onlyNumbers[9:]
            return ans
