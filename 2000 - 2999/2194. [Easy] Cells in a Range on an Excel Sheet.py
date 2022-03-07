# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        startLetter = s[0]
        endLetter = s[3]
        
        startNumber = int(s[1])
        endNumber = int(s[4])
        
        ans = []
        for letter in range(ord(startLetter), ord(endLetter) + 1):
            for num in range(startNumber, endNumber + 1):
                ans.append(chr(letter) + str(num))
                
        return ans 
