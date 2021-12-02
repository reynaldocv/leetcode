# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        sumT = sum(arr)
        if sumT % 3 != 0:
            return False
        sumP = sumT//3
        counter, aux, i = 0, 0, 0
        while i < n:
            aux += arr[i]
            if aux == sumP:
                aux = 0
                counter += 1
            i += 1
        return counter >= 3
            
