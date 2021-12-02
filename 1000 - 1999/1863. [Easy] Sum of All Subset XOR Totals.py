# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

from itertools import permutations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        arr = []
        n = len(nums)
        for i in range(n):
            arr.extend(list(combinations(nums, i + 1)))
        
        ans = 0
        for elem in arr: 
            elem = list(elem)
            aux = elem[0]
            for i in range(1, len(elem)): 
                aux = elem[i]^aux
            ans += aux               
                
        return ans
