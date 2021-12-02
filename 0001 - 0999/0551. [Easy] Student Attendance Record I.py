# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        aux = ""
        counter, counterA = 0, 0
        s += " "        
        n = len(s)
        for i in range(n):
            if s[i] == "A":
                counterA += 1
                if counterA >= 2:
                    return False
            if s[i] != aux:
                if aux == "L":
                    if counter >= 3:
                        return False
                aux = s[i]
                counter = 1
            else: 
                counter += 1
        
        return True
