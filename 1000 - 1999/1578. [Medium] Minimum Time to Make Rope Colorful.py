# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0 
        n = len(colors)
        
        for i in range(n - 1):
            if colors[i] == colors[i + 1]:
                if neededTime[i] <= neededTime[i + 1]:
                    ans += neededTime[i]
                else: 
                    ans += neededTime[i + 1]
                    neededTime[i + 1] = neededTime[i]
                
        return ans
        
