# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans = []
        l = len(candies)
        for i in range(l):
            aux = True if candies[i] + extraCandies >= maxCandies else False
            ans.append(aux)
        return ans
