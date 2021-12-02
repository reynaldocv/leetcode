# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums: 
            dic[num] = dic.get(num, 0) + 1
        
        for i in dic: 
            if dic[i] == 1: 
                return i
        
