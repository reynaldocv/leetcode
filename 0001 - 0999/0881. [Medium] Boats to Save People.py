# https://leetcode.com/problems/boats-to-save-people/
    
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        
        people.sort() 
        
        start = 0 
        end = n - 1 
        
        ans = 0 
        
        while start <= end: 
            ans += 1 
            
            if people[start] + people[end] <= limit: 
                start += 1 
                
            end -= 1 
                
        return ans
                
        
