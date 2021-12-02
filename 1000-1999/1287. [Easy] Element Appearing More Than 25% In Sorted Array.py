# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        dic = {}
        for num in arr: 
            dic[num] = dic.get(num, 0) + 1
        for num in dic: 
            if dic[num] > n/4:
                return num
        
