# https://leetcode.com/problems/avoid-flood-in-the-city/

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1 for rain in rains]
        
        fullLakes = {}
        daysToDry = []
        
        for (day, rain) in enumerate(rains):
            if rain > 0:
                ans[day] = -1
                if rains[day] in fullLakes:
                    idx = bisect_left(daysToDry, fullLakes[rain])
                    
                    if idx == len(daysToDry): 
                        return []
                    
                    ans[daysToDry.pop(idx)] = rain
                    
                fullLakes[rain] = day
            else:
                daysToDry.append(day)
        
        return ans
