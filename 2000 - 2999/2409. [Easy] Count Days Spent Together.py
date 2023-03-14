# https://leetcode.com/problems/count-days-spent-together/

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        @cache 
        def helper(word):
            tmpM = int(word[: 2])
            tmpD = int(word[3: ])
            
            return days[tmpM - 1] + tmpD
            
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30]
        
        for i in range(1, 12):
            days[i] += days[i - 1]
            
        tmp = min(helper(leaveAlice), helper(leaveBob)) - max((helper(arriveAlice), helper(arriveBob))) + 1
            
        return tmp if tmp >= 1 else 0 
            
