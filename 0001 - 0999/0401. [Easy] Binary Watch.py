# https://leetcode.com/problems/binary-watch/

from itertools import permutations
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def hour(leds):
            h, m, ans = 0, 0, ""
            for i in range(4):
                h = h + leds[i]*2**i                
            for i in range(6):
                m = m + leds[i + 4]*2**i
            
            if h < 12:
                ans = str(h) + ":"                
            if m <= 59:
                if m == 0: 
                    ans += "00"
                elif m < 10:
                    ans += "0"+str(m)
                else:
                    ans += str(m)
            return ans
        
        aux = [1]*turnedOn
        aux.extend([0]*(10 - turnedOn))        
        perm = set(permutations(aux, 10))
        ans = []
        for i in perm: 
            j = hour(i)
            if len(j) >= 4:
                ans.append(hour(i))
        ans.sort()
        return ans
