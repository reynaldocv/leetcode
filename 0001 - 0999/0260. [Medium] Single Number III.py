# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        prev = 0 
        
        for num in nums: 
            prev ^= num 
            
        bits = 0 
        
        while prev % 2 == 0: 
            prev //= 2 
            
            bits += 1 
        
        ans = [0, 0]
        
        for num in nums: 
            bit = (num >> bits) % 2 
            
            ans[bit] ^= num
        
        return ans 
        
