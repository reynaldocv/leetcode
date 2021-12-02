# https://leetcode.com/problems/maximum-population-year/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dic = {}
        for (date1, date2) in logs: 
            dic[date1] = dic.get(date1, 0) + 1
            dic[date2] = dic.get(date2, 0) - 1
        
        date = [*dic]
        date.sort()
        maxAux = aux = 0
        ans = 0
        for d in date:
            aux += dic[d]
            if maxAux < aux:
                maxAux = aux
                ans = d
        return ans
                
