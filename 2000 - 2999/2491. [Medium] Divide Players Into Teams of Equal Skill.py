# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        pairs = len(skill)//2
        aSum = sum(skill)
        
        if aSum % pairs != 0: 
            return -1 
        
        sumPair = aSum//pairs
        
        ans = 0 
        
        for num in skill: 
            if num >= sumPair: 
                return -1
            
            tmp = sumPair - num
            
            if tmp in counter: 
                ans += num*tmp
                
                counter[tmp] -= 1 
                
                if counter[tmp] == 0: 
                    counter.pop(tmp)
                    
            else: 
                counter[num] += 1 
                
        if len(counter) == 0: 
            return ans 
        
        else: 
            return -1
            
