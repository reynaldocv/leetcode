# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        units = []
        units.append(["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"])        
        units.append([])
        for i in range(10):
            unit = units[0][i]
            unit = unit.replace("X", "C")                
            unit = unit.replace("V", "L")
            unit = unit.replace("I", "X")            
            units[1].append(unit)
        units.append([])        
        for i in range(10):
            unit = units[0][i]
            unit = unit.replace("X", "M")
            unit = unit.replace("V", "D")
            unit = unit.replace("I", "C")
            units[2].append(unit)
        units.append([])        
        units[3].extend(["", "M", "MM", "MMM"])
        
        ans = ""
        i = 0
        while num > 0: 
            ans = units[i][num % 10] + ans
            num = num//10
            i += 1
        
        return ans
            
