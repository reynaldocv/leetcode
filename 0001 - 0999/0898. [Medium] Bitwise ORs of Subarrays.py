# https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        tmp = set()
        
        for num in arr: 
            tmp = {num|aux for aux in tmp} | {num}
            ans |= tmp
        
        return len(ans)
