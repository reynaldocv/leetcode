# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        
        ans = int((2*n)**.5)
        
        return ans if ans*(ans + 1)//2 <= n else ans - 1
