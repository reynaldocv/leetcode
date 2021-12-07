# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arr = []
        n = len(dist)
        for i in range(n):
            days, res = divmod(dist[i], speed[i])
            days += 1 if res != 0 else 0 
            insort(arr, days)
        
        maxDay = max(arr)
        
        for i in range(1, maxDay + 1):
            if not arr: 
                return i - 1
            
            elif arr[0] >= i: 
                arr.pop(0)
            
                if arr and arr[0] == i: 
                    return i
            
        return maxDay
            
        
class Solution2:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arr = []
        n = len(dist)
        for i in range(n):
            days, res = divmod(dist[i], speed[i])
            days += 1 if res != 0 else 0 
            insort(arr, days)
        
        maxDay = max(arr)
        
        day = 0
        for arriveDay in arr:     
            if arriveDay < day + 1: 
                return day 
            
            day += 1
            
        return day
        
