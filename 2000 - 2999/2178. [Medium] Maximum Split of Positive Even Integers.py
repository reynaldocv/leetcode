# https://leetcode.com/problems/maximum-split-of-positive-even-integers/

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1: 
            return []
        
        even = 2
        aSum = 0 
        ans = []
        while aSum < finalSum: 
            aSum += even
            ans.append(even)
            even += 2 
        
        if aSum > finalSum:             
            elem1 = ans.pop()
            elem2 = ans.pop()
            ans.append(finalSum - (aSum - elem1 - elem2))
            
        return ans
