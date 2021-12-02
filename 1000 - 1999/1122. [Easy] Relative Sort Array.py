# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = {}
        ans = []
        for i in arr1:
            counter[i] = counter.get(i, 0) + 1
        for i in range(len(arr2)):
            for j in range(counter[arr2[i]]):
                ans.append(arr2[i])
            del counter[arr2[i]]
        
        for i in sorted(counter.keys()):
            for j in range(counter[i]):
                ans.append(i)
            del counter[i]
            
        return ans
