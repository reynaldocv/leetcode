# https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for candies in candiesCount: 
            prefix.append(prefix[-1] + candies)
            
        ans = []
        for (candie, day, cap) in queries: 
            ans.append(prefix[candie] < (day + 1)*cap and day < prefix[candie + 1])
            
        return ans 
