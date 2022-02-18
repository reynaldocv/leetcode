# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:        
        ans = []
        n = len(num)
        
        for (i, char) in enumerate(num):
            while ans and ans[-1] > char and len(ans) > i - k:
                ans.pop()
            
            if len(ans) < n - k: 
                ans.append(char)
                
        while ans and ans[0] == "0":
            ans.pop(0)
            
        return "".join(ans) if ans else "0"
                
        
