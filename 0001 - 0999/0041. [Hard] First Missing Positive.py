# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minElem = inf
        maxElem = 0 
        seen = {}
        
        for num in nums: 
            if num > 0: 
                minElem = min(minElem, num)
                maxElem = max(maxElem, num)
                seen[num] = True
        
        if minElem >= 2: 
            return 1
        elif maxElem == len(seen): 
            return maxElem + 1
        else: 
            for num in range(1, maxElem):
                if num not in seen: 
                    return num
        
