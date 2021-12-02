# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic, n = {}, len(nums)
        
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        ans = -1
        for num in dic: 
            if dic[num] > n//2:
                ans = num
        return ans
        
