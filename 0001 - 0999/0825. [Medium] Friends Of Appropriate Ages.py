# https://leetcode.com/problems/friends-of-appropriate-ages/

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        limit = max(ages) + 1
        counter = [0 for i in range(limit)]
        prefix = [0 for i in range(limit)]
        
        for age in ages: 
            counter[age] += 1 
            
        for i in range(1, limit):
            prefix[i] = prefix[i - 1] + counter[i]
            
        ans = 0 
        for x in range(1, limit):
            if x >= 15 and counter[x] > 0: 
                y = x//2 + 7 
                if y <= x:          
                    if y < x:
                        ans += counter[x]*(prefix[x - 1] - prefix[y])                    
                    ans += counter[x]*(counter[x] - 1)
                    
        return ans
