# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        rating = {}
        
        for (idx, rt, vf, pr, dt) in restaurants: 
            if pr <= maxPrice and dt <= maxDistance:                 
                if veganFriendly == 0: 
                    ans.append(idx)
                    rating[idx] = rt
                elif veganFriendly == 1 and vf == 1: 
                    ans.append(idx)
                    rating[idx] = rt

        return sorted(ans, reverse = True, key = lambda item: (rating[item], item))
        
