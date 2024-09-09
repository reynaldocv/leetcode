# https://leetcode.com/problems/convert-date-to-binary/

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        words = date.split("-")
        
        ans = []
        
        for word in words: 
            binary = str(bin(int(word)))[2: ]
            
            ans.append(binary)
            
        return "-".join(ans)
        
