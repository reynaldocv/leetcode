# https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums[:: -1]: 
            while num:
                ans.append(num % 10)
                
                num//= 10 
                
        return ans[:: -1]
