# https://leetcode.com/problems/minimum-genetic-mutation/

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        @cache
        def hamming(start, end):
            counter = 0 
            for (i, char) in enumerate(start):
                if char != end[i]:
                    counter += 1
                
            return counter
        
        @cache
        def helper(start, end, mask):
            if start == end: 
                return 0
            else: 
                ans = inf
                for key in bank: 
                    if hamming(start, key) == 1:
                        if (1 << index[key]) & mask == 0:  
                            aux = helper(key, end, mask ^ (1 << index[key]))
                            ans = min(ans, 1 + aux)
                return ans
                                        
        index = {}
        for (i, gen) in enumerate(bank):
            index[gen] = i
                
        ans = helper(start, end, 0)
        
        return -1 if ans == inf else ans
            
        
        
