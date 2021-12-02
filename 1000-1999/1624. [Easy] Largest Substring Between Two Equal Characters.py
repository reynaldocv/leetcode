# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxPos = {}
        minPos = {}
        n = len(s)
        for i in range(n):
            maxPos[s[i]] = i
            if s[i] not in minPos:
                minPos[s[i]] = i
        ans = -1
        for k in maxPos:
            ans = max(maxPos[k] - minPos[k] - 1, ans)
        
        return ans
        
