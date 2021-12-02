# https://leetcode.com/problems/powerful-integers/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []
        
        expX = 0 if x == 1 else int(log(bound, x))
        expY = 0 if y == 1 else int(log(bound, y))
        ans = set([])
        for i in range(expX + 1):
            for j in range(expY + 1):
                aux = x**i + y**j
                if aux <= bound: 
                    ans.add(aux)
                else:
                    break
        return ans
