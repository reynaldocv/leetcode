# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution:
    def maxDiff(self, num: int) -> int:
        
        strNum = str(num)
        
        old = ""
        for (i, char) in enumerate(strNum):
            if char != "9": 
                old = char
                break
                
        maxNum = strNum.replace(old, "9") if old != "" else strNum
                
        old = ""
        for (i, char) in enumerate(strNum):
            if i == 0: 
                if char != "1": 
                    old = char
                    new = "1"
                    break
            else: 
                if char != strNum[0] and char != "0": 
                    if char != 0:
                        old = char
                        new = "0"
                        break

                
        minNum = strNum.replace(old, new) if old != "" else strNum
        
        return int(maxNum) - int(minNum)
        
        
