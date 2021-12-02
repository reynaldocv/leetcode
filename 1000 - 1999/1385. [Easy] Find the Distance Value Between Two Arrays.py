# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for numA in arr1:
            success = True
            for numB in arr2:
                if abs(numA - numB) <= d:
                    success = False
                    break
            if success: 
                ans += 1
        return ans
        
