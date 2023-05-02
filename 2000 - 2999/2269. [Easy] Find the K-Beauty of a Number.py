# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strNum = str(num) 
        
        n = len(strNum) 
        
        ans = 0 
        
        for i in range(n - k + 1):
            tmp = int(strNum[i: i + k])
            
            if tmp != 0 and num % tmp == 0: 
                ans += 1 
                
        return ans 
        
