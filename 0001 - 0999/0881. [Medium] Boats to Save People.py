# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        ans = 0
        while len(people) >= 2: 
            man1 = people.pop(~0)            
            idx = bisect_left(people, limit - man1 + 1)
            idx -= 1
            if idx != -1:
                people.pop(idx)
            
            ans += 1
            
        return ans + len(people)
    
class Solution2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:        
        people.sort()
        n = len(people)
        
        idx1, idx2 = 0, n - 1
        ans = 0
        
        while idx1 <= idx2:
            ans += 1
            if people[idx1] + people[idx2] <= limit:
                idx1 += 1
            idx2 -= 1
        
        return ans
                
        
