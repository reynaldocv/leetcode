# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = defaultdict(lambda: inf)
        
        for (i, num) in enumerate(arr2):
            index[num] = i 
        
        arr1.sort(key = lambda item: (index[item], item))
        
        return arr1
