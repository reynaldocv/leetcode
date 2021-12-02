# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums: 
            dic[num] = dic.get(num, 0) + 1
            if (dic[num] >= 2):
                return True
        return False
        
