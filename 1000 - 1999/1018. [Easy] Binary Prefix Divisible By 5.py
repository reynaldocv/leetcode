# https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        tmp = 0 
        
        ans = []
        
        for bit in nums: 
            tmp = tmp*2 + bit
            
            ans.append(tmp % 5 == 0)
            
        return ans 
        
        
        
