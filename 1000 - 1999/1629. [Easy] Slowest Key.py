# https://leetcode.com/problems/slowest-key/

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(keysPressed)
        maxTime = releaseTimes[0]
        arrTime = [keysPressed[0]]
        ans = releaseTimes[0]
        
        for i in range(1, n):
            auxTime = releaseTimes[i] - releaseTimes[i - 1]
            if auxTime >= maxTime:                 
                if auxTime == maxTime: 
                    arrTime.append(keysPressed[i])
                else: 
                    arrTime = [keysPressed[i]]
                maxTime = auxTime
        
        arrTime.sort(reverse = True)
        return arrTime[0]
        
