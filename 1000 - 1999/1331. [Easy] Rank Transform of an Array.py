# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        index = {}
        
        idx = 1
        
        for num in sorted(arr):
            if num not in index:
                index[num] = idx
                
                idx += 1
                
        return [index[num] for num in arr]
        
        
        
