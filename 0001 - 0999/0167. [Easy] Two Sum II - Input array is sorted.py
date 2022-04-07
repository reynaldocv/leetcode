# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0 
        end = n - 1
    
        while end - start > 0: 
            if numbers[start] + numbers[end] == target: 
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1 
            else: 
                end -= 1 
                
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        n = len(numbers)
        for i in range(n):            
            B = target - numbers[i]
            if B in seen: 
                return [seen[B], i + 1]
            
            seen[numbers[i]] = i + 1
        
        
