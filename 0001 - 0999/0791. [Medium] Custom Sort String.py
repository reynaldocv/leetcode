https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        index = defaultdict(lambda: inf)
        
        for (i, char) in enumerate(order):
            index[char] = i
        
        arr = [char for char in s]
        
        arr.sort(key = lambda item: index[item])
        
        return "".join(arr)
        
        
