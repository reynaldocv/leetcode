# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        aSum = sum(nums)
        aux = abs(goal - aSum)
        
        if aux % limit == 0:
            return aux//limit
        else: 
            return aux//limit + 1
        
class Solution2:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        aSum = sum(nums)
        aux = abs(goal - aSum)
        
        return ceil(aux/limit)
        
        
