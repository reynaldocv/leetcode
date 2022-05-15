# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strNum = str(num)
        tmp = strNum[: k - 1]
        
        ans = 0
        
        for char in strNum[k - 1: ]:
            tmp += char
            if int(tmp) != 0 and num % int(tmp) == 0:
                ans += 1
            
            tmp = tmp[1: ]
            
        return ans 
        
