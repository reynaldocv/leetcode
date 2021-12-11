# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(strNum):
            ans = ""
            for char in strNum: 
                ans += "1" if char == "0" else "0"
            
            return ans
        
        s = "0"
        for i in range(1, n):
            s = s + "1" + reverse(s[::-1])
            
        return s[k - 1]
        
        
        
                
