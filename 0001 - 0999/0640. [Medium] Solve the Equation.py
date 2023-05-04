# https://leetcode.com/problems/solve-the-equation/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:        
        counter = defaultdict(lambda: 0)
        
        value = {"D": 0, "R": 1}
        
        while True: 
            tmp = ""            
        
            for char in senate: 
                val = value[char]

                if counter[val] == 0: 
                    counter[1 - val] += 1 
                    
                    tmp += char 
                    
                else:
                    counter[val] -= 1 
            
            m = len(tmp)
            
            if tmp[0]*m == tmp: 
                if tmp[0] == "R":
                    return "Radiant"
                
                else: 
                    return "Dire"
            
            senate = tmp             
                        
            
        
        
