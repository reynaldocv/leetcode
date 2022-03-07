# https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def helper(string):
            ans = ""
            for char in string: 
                ans += newStr[char]
                
            return int(ans)
        
        newStr = {str(i): str(val) for (i, val) in enumerate(mapping)}
                  
        nums.sort(key = lambda item: helper(str(item)))
                  
        return nums
