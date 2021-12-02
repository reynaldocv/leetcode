# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        aux = []
        for (a, b) in boxTypes:
            aux.append((b,a))
        aux.sort(reverse = True)
        print(aux)
        
        ans = 0
        for i in range(len(aux)):
            if truckSize < aux[i][1]:
                ans += truckSize*aux[i][0]
                break
            else:
                truckSize -= aux[i][1]
                ans += aux[i][0]*aux[i][1]
        return ans
            
        
