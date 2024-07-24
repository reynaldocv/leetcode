# https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        @cache 
        def helper(word):
            strWord = str(word)
            
            return int("".join([value[char] for char in strWord]))
        
        value = {str(ith): str(val) for (ith, val) in enumerate(mapping)}
        
        arr = [(num, ith) for (ith, num) in enumerate(nums)]
        
        arr.sort(key = lambda item: (helper(item[0]), item[1]))
        
        return [num for (num, _) in arr]
        
        
