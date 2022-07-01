# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
    
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        dic, n = {}, len(nums)
        
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        ans = -1
        for num in dic: 
            if dic[num] > n//2:
                ans = num
        return ans
        
