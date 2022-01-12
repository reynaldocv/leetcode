# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        arr = []
        
        for i in range(n):
            arr.append((plantTime[i], growTime[i]))
            
        arr.sort(reverse = True, key = lambda item: item[1])
        
        ans = last = 0
        for (plant, grow) in arr: 
            last += plant
            ans = max(ans, last + grow)
            
        return ans
