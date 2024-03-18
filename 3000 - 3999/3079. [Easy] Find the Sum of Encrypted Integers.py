# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def helper(strNum):
            n = len(strNum)
            digit = max(char for char in strNum)
            
            return int(digit*n)
        
        ans = 0 
        
        for num in nums: 
            ans += helper(str(num))
            
        return ans 
            
