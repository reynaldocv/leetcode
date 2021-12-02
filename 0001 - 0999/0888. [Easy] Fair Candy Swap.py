# https://leetcode.com/problems/fair-candy-swap/

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        n = len(aliceSizes)
        m = len(bobSizes)
        dic = {bobSizes[x]:True for x in range(m)}
        sumAlice = sum(aliceSizes)
        candies = ((sumAlice) + sum(bobSizes))//2
        for i in range(n):
            aux = candies - (sumAlice - aliceSizes[i])
            if dic.get(aux, False): 
                return (aliceSizes[i], aux)
