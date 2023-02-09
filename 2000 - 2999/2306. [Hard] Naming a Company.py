# https://leetcode.com/problems/naming-a-company/

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for _ in range(26)]
        
        for idea in ideas: 
            first = idea[: 1]
            second = idea[1: ]
            groups[ord(first) - ord("a")].add(second)
            
        ans = 0 
        
        for i in range(25):
            for j in range(i + 1, 26):
                mutual = len(groups[i] & groups[j])
                
                ans += 2*(len(groups[i]) - mutual)*(len(groups[j]) - mutual)
                
        return ans 
                
        
