# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        n = len(numbers)
        for i in range(n):
            B = target - numbers[i]
            if B in dic: 
                return [dic[B], i + 1]
            dic[numbers[i]] = i + 1
        
        
