# https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        
        ans = 0
        for i in dic: 
            if dic[i] == 1:
                ans += i
        
        return ans
