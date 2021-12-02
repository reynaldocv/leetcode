# https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen = defaultdict(lambda: 0)
        
        ans = 0
        for num in answers: 
            seen[num + 1] += 1
            
            if seen[num + 1] == num + 1:
                ans += num + 1
                del seen[num + 1]
                
        return ans + sum([key for key in seen])
        
        
