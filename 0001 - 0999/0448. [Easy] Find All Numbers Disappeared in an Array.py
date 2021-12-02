# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {num:True for num in nums}
        
        ans = []
        for i in range(1, n + 1):
            if i not in dic: 
                ans.append(i)
        return ans
        
        
