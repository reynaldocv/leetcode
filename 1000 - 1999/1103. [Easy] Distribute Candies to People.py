# https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for _ in range(num_people)]
        
        idx = 0 
        value = 1 
        
        while candies: 
            if value <= candies: 
                ans[idx] += value
                
                candies -= value
                
                value +=1
                idx = (idx + 1) % num_people
                
            else: 
                ans[idx] += candies 
                
                candies = 0
                
        return ans
