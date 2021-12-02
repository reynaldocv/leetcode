# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        dic = {}
        n = len(candies)
        for i in range(n):
            dic[candies[i]] = dic.get(candies[i], 0) + 1
            
        return min(n//2, len(dic))
        
