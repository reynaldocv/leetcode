# https://leetcode.com/problems/pyramid-transition-matrix/

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        @cache
        def helper(word, new, i):
            if len(word) == 1: 
                return True 
            
            elif i == len(word) - 1:
                return helper(new, "", 0)
            
            else: 
                for color in triple[word[i: i + 2]]:
                    if helper(word, new + color, i + 1):
                        return True 
                    
                return False
               
        triple = defaultdict(lambda: [])
        
        for word in allowed: 
            triple[word[0: 2]].append(word[2: ])

        return helper(bottom, "", 0)
                    
