# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 0:
            aux = tomatoSlices - 2*cheeseSlices
            if aux >= 0: 
                TJ = aux//2
                TS = cheeseSlices - TJ
                if TS >= 0: 
                    return [TJ, TS]
        return []
