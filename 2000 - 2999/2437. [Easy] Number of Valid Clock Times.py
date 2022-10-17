# https://leetcode.com/problems/number-of-valid-clock-times/

class Solution:
    def countTime(self, time: str) -> int:
        seen = set()
        
        for h in range(24):
            aux = str(h) if h > 9 else "0" + str(h)
            
            for m in range(60):
                tmp = aux + ":"
                tmp += str(m) if m > 9 else "0" + str(m)
                
                seen.add(tmp)
       
        ans = 0 
        
        for key in seen: 
            go = True 
            for (i, char) in enumerate(time):
                if char != ":" and char != "?":
                    print(time, key)
                    
                    if key[i] != char: 
                        go = False
                        break
        
            ans += 1 if go else 0 
            
        return ans 
                    
                    
