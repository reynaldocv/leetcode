# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        def sequence(s):
            if len(s) <= 3: 
                self.ans.append(s)                
            if len(s) == 4:
                self.ans.append(s[0:2])
                sequence(s[2:])
            
            if len(s) >= 5:
                self.ans.append(s[0:3])
                sequence(s[3:])
            
        number = number.replace(" ", "")
        number = number.replace("-", "")
        ans = self.ans = []
        sequence(number)
        
        return "-".join(ans)
