# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = [(-1, 0), (-1, 0)]
        
        for (i, num) in enumerate(nums): 
            maximum.append((num, i))
            
            maximum.sort(reverse = True)
            
            maximum = maximum[: 2]
            
        return maximum[0][1] if maximum[0][0] >= 2*maximum[1][0] else -1
        
