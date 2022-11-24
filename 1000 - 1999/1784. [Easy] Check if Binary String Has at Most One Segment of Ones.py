# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0 
        counter = 0
        for char in s + "0":
            if char == "1":
                cnt += 1 
            else: 
                if cnt > 0: 
                    counter += 1                     
                cnt = 0 
        
        return counter <= 1 
                
