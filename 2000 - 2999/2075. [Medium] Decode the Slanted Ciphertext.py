# https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1: 
            return encodedText
        
        if encodedText == "":
            return ""
        
        m = len(encodedText)//rows
        n = rows
        
        arr = [[char for char in encodedText[k*m: k*m + m]] for k in range(n)]
        
        starts = [(0, i) for i in range(m)]
        
        ans = ""
        for (i, j) in starts: 
            for k in range(n):
                r, s = i + k, j + k
                if 0 <= r < n and 0 <= s < m: 
                    ans += arr[r][s]     
                else: 
                    break
                    
        end = len(ans)
        while ans[end - 1] == " ":
            end -= 1
            
        return ans[:end]
                
        
        
