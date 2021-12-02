# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans + 1 if (len(str(num)) % 2 == 0) else ans
        return ans
        
