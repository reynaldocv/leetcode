# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        aux = str(num)
        pos = aux.find("6")    
        if pos >= 0:
            ans = int(aux[:pos] + "9" + aux[pos + 1:])
        else:
            ans = num
        return ans
            
            
