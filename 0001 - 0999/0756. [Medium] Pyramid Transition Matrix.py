# https://leetcode.com/problems/pyramid-transition-matrix/

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def recursive(bottom, new, i):            
            if len(bottom) == 1: 
                return True
            
            elif i == len(bottom) - 1:
                return recursive(new, "", 0)
            
            else: 
                colours = triple[bottom[i: i + 2]]
                
                for color in colours: 
                    if recursive(bottom, new + color, i + 1):
                        return True
                    
                return False
               
        triple = defaultdict(lambda: [])
        
        for word in allowed: 
            triple[word[0: 2]].append(word[2: ])

        return recursive(bottom, "", 0)
                    
