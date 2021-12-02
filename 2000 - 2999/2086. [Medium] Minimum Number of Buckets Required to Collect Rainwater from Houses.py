# https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/

class Solution:
    def minimumBuckets(self, street: str) -> int:
        
        if street == ".":
            return 0
        
        if street == "H":
            return -1 
        
        if "HHH" in street: 
            return -1 
        
        if street[: 2] == "HH":
            return -1 
        
        if street[-2: ] == "HH":
            return -1 

        return street.count("H") - street.count("H.H")
        
class Solution2:
    def minimumBuckets(self, street: str) -> int:
        heap = []
        n = len(street)
        houses = {}
        for (i, char) in enumerate(street):
            cnt = 0 
            if char == ".":
                if i < n - 1 and street[i + 1] == "H":
                    cnt += 1                    
                if 0 < i and street[i - 1] == "H":
                    cnt += 1   
                
                heappush(heap, (-cnt, i))                    
            else: 
                houses[i] = True
       
        if not heap and "H" in street: 
            return - 1
        
        ans = 0 
        while heap: 
            (cnt, idx) = heappop(heap)
            print(cnt, idx, ans)
            if cnt == -2: 
                if idx - 1 in houses and idx + 1 in houses: 
                    ans += 1
                    houses.pop(idx - 1)
                    houses.pop(idx + 1)
                elif idx - 1 in houses or idx + 1 in houses:
                    heappush(heap, (-1, idx))
            elif cnt == -1: 
                if idx - 1 in houses:
                    houses.pop(idx - 1)
                    ans += 1
                elif idx + 1 in houses: 
                    houses.pop(idx + 1)
                    ans += 1
                    
        return -1 if len(houses) > 0 else ans
