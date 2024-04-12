# https://leetcode.com/problems/largest-number-after-mutating-substring/

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num) 
        
        newNum = [str(num) for num in change]
        
        start = 0         
        ans = ""
        
        while start < n and num[start] >= newNum[int(num[start])]:
            ans += num[start]
            
            start += 1 
        
        while start < n and num[start] <= newNum[int(num[start])]:
            ans += newNum[int(num[start])]
            
            start += 1 
            
        while start < n:
            ans += num[start]
            
            start += 1 
            
        return ans 
        
