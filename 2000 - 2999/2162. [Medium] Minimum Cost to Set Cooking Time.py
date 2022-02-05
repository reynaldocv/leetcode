# https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def helper(start, arr):
            if not arr: 
                return 0 
            elif arr[0] == start: 
                return pushCost + helper(arr[0], arr[1:])
            else: 
                return moveCost + pushCost + helper(arr[0], arr[1:])
            
        ans = inf
        seconds = targetSeconds % 60
        minutes = (targetSeconds - seconds)//60
        
        tmp = []
            
        if minutes < 100: 
            arr = [minutes//10, minutes%10, seconds//10, seconds%10]
            while arr[0] == 0:
                arr.pop(0)

            tmp.append(arr)
            
        if seconds <= 39:
            seconds += 60
            minutes -= 1 
            arr = [minutes//10, minutes%10, seconds//10, seconds%10]
            while arr[0] == 0:
                arr.pop(0)

            tmp.append(arr)
            
        for arr in tmp:             
            ans = min(ans, helper(startAt, arr))

        return ans
