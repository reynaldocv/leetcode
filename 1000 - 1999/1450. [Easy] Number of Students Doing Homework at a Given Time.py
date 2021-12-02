# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        l = len(startTime)
        ans = 0
        for i in range(l):
            if (startTime[i] <= queryTime <= endTime[i]):
                ans += 1
        return ans
            
